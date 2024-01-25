import requests
import time
from bs4 import BeautifulSoup

# 存入資料庫模組
from utils.access_database import get_database
# 取得 href 模組
from utils.get_href import get_href
# 自動化瀏覽器設定模組
from utils.operator_browser.chrome import create_chrome_driver


domain = "https://www.songshanculturalpark.org"
url = "https://www.songshanculturalpark.org/exhibition"



# 用 selenium 開啟瀏覽器
try:
    driver = create_chrome_driver()
    driver.get(url)
    # 取得網頁原始碼
    content = driver.page_source  

    # 解析原始碼
    soup = BeautifulSoup(content, 'html.parser')

    # 取得所有展覽的 a tag
    exhibitionLinks = soup.find_all('a', class_='btn')

    # 建立一個 dict 來存放所有的展覽資訊
    result = []
    hrefs = get_href(exhibitionLinks)
    # todo 優化篩選: 此案例第一個值為無效值，所以先 pop 掉
    valid_hrefs = [link for link in hrefs if link.startswith('/exhibition')]
    print(valid_hrefs,"篩選結果")
    # 用迴圈跑每個展覽頁面內容
    for href in valid_hrefs:
        exhibition = {}
        target = domain + href
        print(target)
        # 應對網站反爬蟲機制，等待載入結束，目前抓 10 秒
        driver.implicitly_wait(10)
        driver.get(target)
        content = driver.page_source  # 取得網頁原始碼
        soup = BeautifulSoup(content, 'html.parser')
        # 取得展覽標題
        title = soup.find('p', class_='inner_title')
        exhibition['title'] = title.text
        # 取得展覽日期
        date = soup.find('p', class_='montsrt')
        exhibition['date'] = date.text
        # 取得展覽時間
        # time = soup.find('div', class_='time')
        # exhibition['time'] = time.text
        # 取得展覽地點
        location = soup.find('p', class_='place')
        exhibition['location'] = location.text
        # todo 取得展覽內容
        # content = soup.find('div', class_='content')
        # exhibition['content'] = content.text
        # # todo 取得展覽圖片
        # image = soup.find('img', class_='image')
        # exhibition['image'] = image.img['src']
        # # 取得展覽票價
        # price = soup.find('div', class_='price')
        # exhibition['price'] = price.text
        # # 取得展覽連結
        # exhibition['href'] = target
        # 將展覽資訊存入 result
        result.append(exhibition)

    print(result,"結果")
    

except Exception as e:
    print(e)
    driver.close()
    print('=======================')
    print('爬蟲失敗')
    print('=======================')
    result = []


