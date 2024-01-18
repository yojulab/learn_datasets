from selenium import webdriver
path_browser = "../../chromedriver"
browser = webdriver.Chrome(path_browser)

# keyword : 축제
url = 'https://korean.visitkorea.or.kr/search/search_list.do?keyword=%EC%B6%95%EC%A0%9C'
browser.get(url)
import time
time.sleep(2)  

from selenium.webdriver.common.by import By
browser.find_element(By.CSS_SELECTOR, '#sorting_options > button.option').click()
time.sleep(1)
browser.find_element(By.XPATH, '//span[text()="#문화관광축제"]').click()
time.sleep(2)  

from visitkorea_trip_functions import get_content
try :
    elements = browser.find_elements(By.CSS_SELECTOR, 'div.area_txt')
    data_bundle = list()
    for element in elements:
        element.find_element(By.CSS_SELECTOR, 'a').click()
        time.sleep(2)
        html = browser.page_source
        row = get_content(html)
        data_bundle.append(row)
        browser.back()
        time.sleep(2)
except :
    pass
finally :
    browser.quit()

if data_bundle :
    from visitkorea_trip_functions import get_content, store_datas

    columns = ['title', 'subtitle', 'startdate','enddate','telephone','homepage','address','eventplace','host','organizer','usagefee','eventtime','describe']
    store_datas(data_bundle, columns)

pass