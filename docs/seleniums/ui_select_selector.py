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

# - 주소 https://www.w3schools.com/ 입력                                                             # 1
browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")

# - 가능 여부에 대한 OK 받음 (ok를 주고받는 네트워크 상 번호는 200이다.)
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
#refer official = "https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select"
from selenium.webdriver.support.ui import Select                                                     # 6
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)                              # 6
#국가 selectbox 선택
selector_element = "#country"                                                                        # 3 ---------------------selector 값
element_country = browser.find_element(by=By.CSS_SELECTOR, value = selector_element )                # 2
Select(element_country).select_by_index(1)                                                           # 7 ---------------------selector에서 두번째 것을 선택하도록 함
#주 selectbox 선택
selector_element = "#state"                                                                          # 5---------------------selector 값
element_state = browser.find_element(by=By.CSS_SELECTOR, value = selector_element )                  # 4
Select(element_state).select_by_index(1)                                                             # 7 ---------------------selector에서 두번째 것을 선택하도록 함
pass
# browser.save_screenshot("./formats.png")

# 브라우저 종료
browser.quit()