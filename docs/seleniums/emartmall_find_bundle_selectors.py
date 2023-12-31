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
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# - 가능 여부에 대한 OK 받음


# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.mnemitem_unit"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value = selector_value)

for element_item in element_bundle :               #for element_item in element_bundle[10:41] ---> 리스트에서 10~41 사이에서 looping 을 함. 오류를 찾을대 사용. #list slicing 기법임.
    # 상품 제목
    print("{}".format(element_item.text))
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value ="span.mnemitem_goods_tit")
    title = element_title.text
    
    # 상품 판매 원가 

    # 데이터베이스를 받을 때 old_price 라는 tag가 없을때 오류 나면 대처법으로  try,except 구문이 있음.

    try :##################################################################################################################            try 에는 정식으로 코드를 집어넣음.
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value ="div > del > em")
        old_price = element_old_price.text
        pass
    except:
        old_price = ""          # 방어 코드임. old price에 값이 없으면 나는 오류를 해결해주는 코드.
        pass
    finally:
        pass

    print("title : {}, old price : {}".format(title,old_price))
# 브라우저 종료
browser.quit()