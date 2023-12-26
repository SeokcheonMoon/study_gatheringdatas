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
browser.get("https://pedia.watcha.com/ko-KR/contents/m5ZlbBL/comments")

# - 가능 여부에 대한 OK 받음 (ok를 주고받는 네트워크 상 번호는 200이다.)
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 한페이지씩 이동하기
element_body = browser.find_element(by = By.CSS_SELECTOR, value = "body")

previous_scrollHeight= 0
while True :
    element_body.send_keys(Keys.END)                                                        # scroll 길게 함

    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")      # 현재의 scrollheight를 while문 안에 넣어 반복하여 길게 함.
    if previous_scrollHeight >= current_scrollHeight :
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass
# browser.save_screenshot("./formats.png")

# 브라우저 종료
browser.quit()