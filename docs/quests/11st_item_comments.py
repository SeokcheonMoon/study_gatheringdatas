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

# - 주소 11번가 입력
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=8&dispCtgrNo=1001327"
browser.get(url)

####################################################################################################################

def connection() :                                                          #mongoDB connect function
    from pymongo import MongoClient

    # mongoDB에 접속 ( 자원에 대한 class)
    mongoClient = MongoClient("mongodb://localhost:27017") #해당하는 mongoDB의 주소를 변수에 담아준다.


    # database 생성 및 연결
    database = mongoClient["gatheringdatas"]



    # collection에 작업
    collection = database["11st_comments"]

    return collection

pass

####################################################################################################################


# - 정보 획득
from selenium.webdriver.common.by import By

elements_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.box_pd.ranking_pd > a")        # 상품 한칸

pass
# browser.save_screenshot("./formats.png")

for index in range(4) :
    elements_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.box_pd.ranking_pd > a")
    elements_items[index].click()
    time.sleep(3)       #화면 완성 term
    element_title = browser.find_element(by=By.CSS_SELECTOR, value = "h1.title")                    #명칭
    title = element_title.text

    # elements_image = browser.find_element(by=By.CSS_SELECTOR, value = "div.expand_target")          #이미지
    # image = elements_image.text

    try :
        elements_price = browser.find_element(by=By.CSS_SELECTOR, value = "dd.price_regular")       #원가
        price = elements_price.text
        pass
    except:
        price = ""          
        pass
    finally:
        pass

    elements_sale = browser.find_element(by=By.CSS_SELECTOR, value = "dd.price")                      #판매가
    sale = elements_sale.text
    elements_info = browser.find_element(by=By.CSS_SELECTOR, value = "table.prdc_detail_table")         # 상품정보
    info = elements_info.text

    print("명칭 : {}".format(title))
    # print("이미지 : {}".format(image))
    print("원가 : {}".format(price))
    print("판매가 : {}".format(sale))
    print("상품정보 : {}".format(info))
    
    browser.back()
    time.sleep(3)       #화면 완성 term
    pass
pass

# 브라우저 종료
browser.quit()