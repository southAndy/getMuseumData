import requests
from bs4 import BeautifulSoup

url = 'https://montue.ntue.edu.tw/exhibitions/'
response = requests.get(url)
# 如果回傳值是 200 代表請求成功
if response.status_code == 200:
    # 將回傳值的文字內容取出
    museumContent = BeautifulSoup(response.text, 'html.parser')
    # 取出展覽文章標題
    titles = museumContent.find_all('div', class_='text')
    print(titles)
    # 將資料整理成 json 格式

    # with open('ptt-stock.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)


# 檔案名稱: ptt-stock.html
# 開啟檔案
# 寫入檔案
