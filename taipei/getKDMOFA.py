import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import json

url = 'https://www.huashan1914.com/w/huashan1914/exhibition?typeId=17111317255246856'
chromeDriverPath = './chromedriver-mac-arm64/chromedriver'
s = Service(chromeDriverPath)

# 用 selenium 開啟瀏覽器
try:
    driver = webdriver.Chrome(service=s)    
    driver.get(url)
    content = driver.page_source # 取得網頁原始碼
    # get a tag in content

    soup = BeautifulSoup(content, 'html.parser')
    aTags = soup.find_all('li', class_='item-static')
    # get a tag in li
    # for aTag in aTags:
    for tag in content:
        print(tag)

    
    time.sleep(100000) # 100 秒後關閉瀏覽器

except Exception as e:
    print(f"Error: {e}")
# 用 selenium 去開啟網頁


# response = requests.get(url)
# result = {"hitRate": 0, "UID": 0, }
# # 如果回傳值是 200 代表請求成功
# if response.status_code == 200:
#     # 將回傳值的文字內容取出
#     museumContent = BeautifulSoup(response.text, 'html.parser')
#     # 取出展覽文章標題
#     titles = museumContent.find('div', class_='BigTitle')
#     result['title'] = titles.text
#     # 取出展覽日期
#     dates = museumContent.find('div', class_='SDate')
#     result['date'] = dates.text
#     # 取出展覽圖片 src (如果有的話)
#     if museumContent.find('div', class_='TopBnrArea2'):
#         images = museumContent.find('div', class_='TopBnrArea2')
#         result['image'] = images.find('img')['src']
#     else:
#         images = ''
#         result['image'] = ''
#     # 取出展覽內容
#     contents = museumContent.find('div', class_='CRow')
#     result['content'] = contents.text

# # 存成 json 檔案
# with open('MOFA.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=2)
