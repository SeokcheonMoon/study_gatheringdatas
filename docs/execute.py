# * 웹 크롤링 동작
from selenium import webdriver

driver_path = "chromedriver.exe"
# ChromeDriver 실행
browser = webdriver.Chrome(executable_path=driver_path)