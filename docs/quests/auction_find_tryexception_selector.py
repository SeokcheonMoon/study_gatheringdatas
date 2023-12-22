#상품 제목
#판매 원가
#변경 가격
#배송 방법
#공유: github, 각각 사용한 element

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소입력
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx?catetab=1")

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

for element_item in element_bundle :               
    # 상품 제목
    print("{}".format(element_item.text))
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value ="div.info>em>a")
    title = element_title.text
    
    # 상품 판매 원가 

    try :
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value ="span.cost")
        old_price = element_old_price.text
        pass
    except:
        old_price = ""          
        pass
    finally:
        pass


    element_sales = element_item.find_element(by=By.CSS_SELECTOR, value ="span.sale")
    sales = element_sales.text
    
    try :
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value ="div.item_icons > div")
        delivery = element_delivery.text
        delivery_list = []
        delivery_list.append(delivery)
    except:
        delivery = ""          
        pass
    finally:
        pass

    
    print("title : {}, old price : {}, sales : {}, delivery: {}".format(title,old_price,sales,delivery_list))
    
# 브라우저 종료
browser.quit()