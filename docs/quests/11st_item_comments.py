#다 못한거

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

elements_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.box_pd.ranking_pd > a")        # 상품 한칸 정보들을 리스트 변수에 담음

pass
# browser.save_screenshot("./formats.png")

for index in range(4) :

def item() :
    elements_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.box_pd.ranking_pd > a")
    elements_items[index].click()
    time.sleep(3)       #화면 완성 term
    element_title = browser.find_element(by=By.CSS_SELECTOR, value = "h1.title")                    #명칭
    title = element_title.text

    elements_image = browser.find_element(by=By.CSS_SELECTOR, value = "div.img_full > img")          #이미지
    image = elements_image.get_attribute('src')

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


    
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    
    # webdriver_manager_directory = ChromeDriverManager().install()
    # browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    
    browser.switch_to.frame("ifrmReview")
    main = "review-list-area"

    element_body = browser.find_elements(by = By.CSS_SELECTOR, value = main)

    time.sleep(2)
    while True:
        try:
            # 버튼이 나타날 때까지 기다리고, 나타나면 클릭
            # (10초는 예시로, 필요에 따라 적절한 시간으로 조절하세요.)
            element_more_button = browser.find_element(by = By.CSS_SELECTOR, value = "#review-list-page-area > div > button")
            element_more_button.click()
            time.sleep(3)
        except :
            # 더 이상 버튼이 없으므로 while문을 종료
            break

    selector_value = "li.review_list_element"
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

    for element_item in element_bundle : 

        name = element_item.find_element(by = By.CSS_SELECTOR, value = "dt.name" )                     # 작성자 list
        names = name.text
        # option = element_item.find_element(by = By.CSS_SELECTOR, value = "" )                   # 선택옵션 list
        # options = option.text
        star = element_item.find_element(by = By.CSS_SELECTOR, value = "div > p.grade > span > span" )               # 별점 점수 list
        stars = star.text
        try :
            comment = element_item.find_element(by = By.CSS_SELECTOR, value = "div > div > div.cont_text_wrap > p" )         # 내용 list   
            comments = comment.text
            pass
        except:
            comments = ""          
            pass
        finally:
            pass



    # print("명칭 : {}".format(title))
    # print("이미지 : {}".format(image))
    # print("원가 : {}".format(price))
    # print("판매가 : {}".format(sale))
    # print("상품정보 : {}".format(info))

    print("name : {}".format(names))
    print("star : {}".format(stars))
    print("comment : {}".format(comments))

    browser.back()
    time.sleep(3)       #화면 완성 term
    pass




# 브라우저 종료
browser.quit()