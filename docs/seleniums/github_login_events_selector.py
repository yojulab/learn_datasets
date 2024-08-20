# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/)
browser.get("https://github.com/login")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

element_login_field = browser.find_element(by=By.CSS_SELECTOR, value="#login_field")
element_login_field.send_keys("otter.oh@gmail.com")

element_password_field = browser.find_element(by=By.CSS_SELECTOR, value="#password")
element_password_field.send_keys("*")

element_login_button = browser.find_element(by=By.CSS_SELECTOR, value="div > input.btn.btn-primary.btn-block.js-sign-in-button")
element_login_button.click()
pass
# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()