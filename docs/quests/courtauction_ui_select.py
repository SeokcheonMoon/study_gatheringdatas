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
browser.get("https://www.courtauction.go.kr/")                                                       #url 가장 먼저 입력          끝

# - 가능 여부에 대한 OK 받음 (ok를 주고받는 네트워크 상 번호는 200이다.)
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

####################################################################################################################

def connection() :                                                          #mongoDB connect function
    from pymongo import MongoClient

    # mongoDB에 접속 ( 자원에 대한 class)
    mongoClient = MongoClient("mongodb://localhost:27017") #해당하는 mongoDB의 주소를 변수에 담아준다.


    # database 생성 및 연결
    database = mongoClient["gatheringdatas"]



    # collection에 작업
    collection = database["courtauction_ui_select"]

    return collection

####################################################################################################################

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

browser.switch_to.frame("indexFrame")

element_auction_items = browser.find_element(by = By.CSS_SELECTOR, value = "#menu > h1:nth-child(5) > a")                # head 에 경매물건
element_auction_items.click()



for court_number in range(3) : 
    selector_element = "#idJiwonNm"                                                                        #법원 
    element_courthouse = browser.find_element(by=By.CSS_SELECTOR, value = selector_element)
    courthouse_bundle = element_courthouse.text
    courthouse = courthouse_bundle.split()            
    Select(element_courthouse).select_by_index(court_number)  
    print("{}".format(courthouse[court_number]))

# selector_element = "#idJpDeptCode"                                                                     #소재지
# element_courthouse = browser.find_element(by=By.CSS_SELECTOR, value = selector_element )        
# Select(element_courthouse).select_by_index(2)  
    
    element_search = browser.find_element(by = By.CSS_SELECTOR,value = "#contents > form > div.tbl_btn > a:nth-child(1) > img")          # 검색기능
    element_search.click()


    total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.page2 > a > span")  

    for page_number in range(len(total_page)+1) :                                                      #페이지 넘버 별로 클릭하기 위해 순서
        total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.page2 > a > span")  
        
        element_number = browser.find_elements(by = By.CSS_SELECTOR,value = "table.Ltbl_list > tbody > tr > td:nth-child(2)")                    #사건번호
        element_location = browser.find_elements(by = By.CSS_SELECTOR,value = "td:nth-child(4)")                    #소재지
        for index in range(len(element_number)) :                                                                 #사건번호 소재지 갯수만큼 출력

            number = element_number[index].text
            location = element_location[index].text
            
            print("{}".format(number))
            print("{}".format(location))
            collection_comments = connection()
            collection_comments.insert_one({ "법원소재지" : courthouse[court_number], "사건번호" : number, "소재지및내역" : location})
        if page_number < len(total_page) :
            total_page[page_number].click()
        else:
            break
    element_search = browser.find_element(by = By.CSS_SELECTOR,value = "div > div > a:nth-child(5) > img")          # 이전기능
    element_search.click()

    pass



pass
# browser.save_screenshot("./formats.png")

# 브라우저 종료
browser.quit()