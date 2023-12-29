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

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")             #1

from selenium.webdriver.common.by import By
# 모달 화면 띄우기 : 평가 및 리뷰 클릭
selector_element = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button"            #2
element_button = browser.find_element(by=By.CSS_SELECTOR, value = selector_element)                                    #3
element_button.click()                                                                                                 #4

# - 정보 획득
# 댓글 모달 확ㅇ인 :(css overflow:scroll or auto)div.fysCi
selector_element = "div.fysCi"                                                                                          #5
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value = selector_element)                              #6

# 댓글 개수 확인 : div.RHo1pe
selector_element = "div.RHo1pe"                                                                                         #12
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value = selector_element)                                  #13
print("count comment before done scoll : {}".format(len(elements_comment)))                                             #14
# scrollableDiv.scrollHeight
# scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);
previous_scrollHeight = 0
while True:                                                                                                              #7
    # print({"scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);"}.format())                                           #8
    # print({"{}, scrollableDiv.scrollHeight);"}.format(element_scrollableDiv))                                            #9
    
    
    # print("{0}.scrollTo({1},{0}.scrollHeight)".format(element_scrollableDiv,previous_scrollHeight))                      #10 
    
    #자바스크립트와 파이썬 결합 방식
    # arguments[0] = scrollableDiv
    # arguments[1] = 0
    browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);"                                       #11
                           ,element_scrollableDiv,previous_scrollHeight)
    # arguments[0] = document.body
    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight",element_scrollableDiv)
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

#스크롤 후 댓글 개수 확인 : div.RHo1pe
selector_element = "div.RHo1pe"                                                                                         #15
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value = selector_element)                                  #16
print("count comment before done scoll : {}".format(len(elements_comment)))                                             #17

pass
# browser.save_screenshot("./formats.png")

# 브라우저 종료
browser.quit()