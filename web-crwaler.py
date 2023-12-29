import requests
from bs4 import BeautifulSoup

url = 'https://www.tfam.museum/index.aspx?ddlLang=zh-tw'
response = requests.get(url)
# 如果回傳值是 200 代表請求成功
if response.status_code == 200:
    # 並將其儲存到檔案中
    with open('ptt-stock.html', 'w', encoding='utf-8') as file:
        file.write(response.text)


# 檔案名稱: ptt-stock.html
# 開啟檔案
# 寫入檔案
