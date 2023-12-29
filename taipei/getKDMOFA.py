import requests
from bs4 import BeautifulSoup
import json

url = 'https://kdmofa.tnua.edu.tw/mod/exhibition/index.php?REQUEST_ID=e1626ae68798853bcff9a390f902a9dfbd0b47c33f2781289d71a04afc3631a3'


response = requests.get(url)
result = {"hitRate": 0, "UID": 0, }
# 如果回傳值是 200 代表請求成功
if response.status_code == 200:
    # 將回傳值的文字內容取出
    museumContent = BeautifulSoup(response.text, 'html.parser')
    # 取出展覽文章標題
    titles = museumContent.find('div', class_='BigTitle')
    result['title'] = titles.text
    # 取出展覽日期
    dates = museumContent.find('div', class_='SDate')
    result['date'] = dates.text
    # 取出展覽圖片 src (如果有的話)
    if museumContent.find('div', class_='TopBnrArea2'):
        images = museumContent.find('div', class_='TopBnrArea2')
        result['image'] = images.find('img')['src']
    else:
        images = ''
        result['image'] = ''
    # 取出展覽內容
    contents = museumContent.find('div', class_='CRow')
    result['content'] = contents.text

# 存成 json 檔案
with open('MOFA.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
