import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import sys
import os
# 存入資料庫
from utils.access_database import get_database

url = 'https://www.huashan1914.com/w/huashan1914/exhibition?typeId=17111317255246856'
chromeDriverPath = './chromedriver'
s = Service(chromeDriverPath)
load_dotenv()
print(os.getenv('HUA_SHAN_CONFIG'))
web_Prefix = os.getenv('HUA_SHAN_CONFIG')

# 模仿瀏覽器設定
options = Options()
options.add_argument("--disable-notifications")

# 用 selenium 開啟瀏覽器
try:
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(url)
    content = driver.page_source  # 取得網頁原始碼
    # get a tag in content

    soup = BeautifulSoup(content, 'html.parser')
    exhibitionTags = soup.find_all('li', class_='item-static')

    # 寫一個陣列來存放所有的展覽 href
    hrefs = []
    # 取得裡面的 a tag
    for aTag in exhibitionTags:
        aTag = aTag.find('a')
        # 取得 a tag 的 href，並存入陣列
        hrefs.append(aTag['href'])

    # 建立一個 dict 來存放所有的展覽資訊
    result = []
    # 進入每個展覽的網頁
    for href in hrefs:
        exhibition = {}
        target = web_Prefix + href
        print(target)
        driver.get(target)
        content = driver.page_source  # 取得網頁原始碼
        soup = BeautifulSoup(content, 'html.parser')
        # 取得展覽標題
        title = soup.find('div', class_='article-title')
        exhibition['title'] = title.text
        # todo 取得展覽日期（需整理）
        date = soup.find_all('div', class_='card-date')
        exhibition['date'] = date[0].text
        # 取得營業時間
        time = soup.find('div', class_='card-time')
        exhibition['time'] = time.text
        # 取得展覽圖片
        image = soup.find('li', class_='flex-active-slide')
        # for img in image:
        #     print(img['src'])
        if image:
            image = image.find('img')['src']
            print(image)
        else:
            print('no image')
        # 取得展覽內容
        content = soup.find('div', class_='card-text-info')
        exhibition['content'] = content.text
        # todo 取得主辦資訊（需整理）
        host = soup.find('div', class_='card-text-info')
        exhibition['host'] = host.text

        # 將每個展覽的資訊存入 result 陣列
        result.append(exhibition)
    get_database(result)

    # 100 秒後關閉瀏覽器
    time.sleep(100000)

except Exception as e:
    print(f"Error: {e}")
