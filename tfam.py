import requests
import time
from bs4 import BeautifulSoup

# 存入資料庫模組
from utils.access_database import get_database
# 取得 href 模組
from utils.get_href import get_href
# 自動化瀏覽器設定模組
from utils.operator_browser.chrome import create_chrome_driver


hrefs = ['/Exhibition/Exhibition_Content.aspx?ddlLang=zh-tw&id=745','/Exhibition/Exhibition_Content.aspx?ddlLang=zh-tw&id=746','/Exhibition/Exhibition_Content.aspx?ddlLang=zh-tw&id=747']
url = "https://www.tfam.museum/Exhibition/Exhibition.aspx?ddlLang=zh-tw"
domain = "https://www.tfam.museum"

try:
    driver = create_chrome_driver()
    result = []
    driver.get(url)
    time.sleep(10)
    for href in hrefs:

        # 每個展覽的資訊
        exhibition = {}
        targetUrl = domain + href
        driver.get(targetUrl)

        # 用 BS4 取得的各架構
        content = driver.page_source  
        soup = BeautifulSoup(content, 'html.parser')

        title = soup.find('span', id='CPContent_lbExName')
        date = soup.find('span', id='CPContent_lbDate')
        content = soup.find('div', class_='info-content')
        descriptionFilterHtml = soup.find_all('p')
        element = soup.find('div', id='banner')
        style = element.get('style')

        # 存入 dict
        exhibition = {
            'title': title.text,
            'category': None, # 後續功能
            'startDate': date.text,
            'endDate': None,
            'descriptionFilterHtml': descriptionFilterHtml.text,
            'location': {
                'address': None,
                'latitude': None,
                'longitude': None,
            },
            'time': None,
            'hitRate':0,
            'imageUrl':None,
            'comments':[],
            'price':None,
            'officialUrl':None,
            'officialPhone':None,
        }
        print(exhibition,'============  爬蟲結果 =============')
        result.append(exhibition)
    driver.close()

except Exception as e:
    print(e)
    driver.close()
    print('=======================')
    print('爬蟲失敗')
    print('=======================')
    result = []