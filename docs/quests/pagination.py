# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# 브라우저 설치

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력

for page_number in range(1,11) :  # page number                          
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
    # - html 파일 받음(and 확인)
    html = browser.page_source
    pass

pass
# - html 파일 받음(and 확인)

# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By


pass
# browser.save_screenshot("./formats.png")

# 브라우저 종료
browser.quit()