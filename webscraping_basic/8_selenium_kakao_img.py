from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 
options.add_argument('headless') # headless 사용
options.add_argument('window-size=1920x1080') # 브라우저의 크기
# HeadlessChrome으로 탐지되는 것을 방지
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36") 
driver = webdriver.Chrome("./chromedriver", chrome_options=options)
driver.get("https://place.map.kakao.com/10821532") # 웝페이지 불러오기
time.sleep(1) # 1초동안 기다림

driver.find_element(By.CLASS_NAME , "link_photo").click() # 사진 한장을 클릭하여 이미지 모달을 킴
time.sleep(1) # 1초동안 기다림

for i in range(1,11): # 10개의 이미지 링크를 불러옴
    driver.find_element(By.XPATH, "//*[@id='photoViewer']/div[2]/div[2]/div/ul/li[{}]".format(i)).click() # 이미지 썸네일 클릭
    print(driver.find_element(By.CLASS_NAME , "img_photo").get_attribute("src"))# 이미지 주소를 불러옴
    
driver.quit()

