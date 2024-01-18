import time
import requests
import io
import os
from selenium import webdriver
import hashlib

def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls

from PIL import Image
def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")    

def search_and_download(search_term:str,driver_path:str,target_path='./pictures',number_images=5, number_train=0):
    t0 = time.time()
    # for test
    target_folder = os.path.join(target_path,'test','_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):       # for test
        os.makedirs(target_folder)

    train_folder = str()
    if number_train > 0 and number_train < number_images : # for train
        train_folder = os.path.join(target_path,'train','_'.join(search_term.lower().split(' ')))
        if not os.path.exists(train_folder):       # for test
            os.makedirs(train_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
        count = 0
        try:
            for elem in res:
                store_folder = str()
                count = count + 1
                if train_folder and number_train >= count:
                    store_folder = train_folder
                else :
                    store_folder = target_folder
                persist_image(store_folder,elem)    
        except :
            pass

    t1 = time.time()
    total_time = t1 - t0
    

# Main block
def main():
    chromedriver = '../chromedriver'
    # target_path = '/Users/sanghunoh/Download/images'
    t0 = time.time()
    # human face status
    # search_keys = ['happy human face', 'sad human face', 'excited human face', 'boring human face',]
    # self drive car
    search_keys = ['stop signal', 'traffic light', 'road crossing', 'whole body',]
    number_images = 60
    number_train = 10       # number_images > number_train
    for key in search_keys:
        search_and_download(search_term=key, driver_path=chromedriver, number_images=number_images, number_train=number_train)
    t1 = time.time()
    total_time = t1 - t0
    print(f'Total time is {str(total_time)} seconds.')

if __name__ == '__main__':
    main()        