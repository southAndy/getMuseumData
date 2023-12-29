import requests
from bs4 import BeautifulSoup

url = 'https://kdmofa.tnua.edu.tw/mod/exhibition/index.php?REQUEST_ID=e1626ae68798853bcff9a390f902a9dfbd0b47c33f2781289d71a04afc3631a3'


response = requests.get(url)
# 如果回傳值是 200 代表請求成功
if response.status_code == 200:
    # 將回傳值的文字內容取出
    museumContent = BeautifulSoup(response.text, 'html.parser')
    # 取出展覽文章標題
    titles = museumContent.find_all('div', class_='BigTitle')
    print(titles)
    # 將資料整理成 json 格式
    # {"title": "xxx", "date": "xxx", "location": "xxx", "img": "xxx"}

    # with open('ptt-stock.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)


# 檔案名稱: ptt-stock.html
# 開啟檔案
# 寫入檔案
