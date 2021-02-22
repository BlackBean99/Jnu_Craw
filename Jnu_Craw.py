import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

url = "http://sw.jnu.ac.kr/user/indexSub.action?codyMenuSeq=19210&siteId=sw_new&menuUIType=top"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('lang=ko')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('C:\\workspace\chromedriver.exe',options=options)

driver.get(url)
try: 
    news_list = []
    news_data = driver.find_elements_by_class_name('title')
    for i in news_data:
        news_list.append(i.text.split('\n'))
    
    date_list = []
    for l in range(1,61):
        date_data = driver.find_elements_by_xpath("//*[@id=\"board-container\"]/div[4]/form[1]/table/tbody/tr["+str(l)+"]/td[4]")
        # empty_list = []
        for n in date_data:
            date_list.append(n.text.split('\n'))
    
    for x,y in zip(date_list, news_list):
        print(x,y)
            
    data = pd.DataFrame(list(zip(date_list, news_list)),columns=['작성일','공지사항'])
    print(data)
    data.to_csv('file.csv',encoding='utf-8-sig')

except TimeoutException:
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')
finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()