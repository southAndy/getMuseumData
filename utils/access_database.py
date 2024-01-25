from pymongo import MongoClient
# 引入環境變數
from dotenv import load_dotenv
import os


def get_database(data):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    load_dotenv()
    database_url = os.getenv('DB_URL_LOCAL')
    CONNECTION_STRING = database_url

    # 連線對應的資料庫
    client = MongoClient(CONNECTION_STRING)

    # 切換到展覽資料庫
    exhibitionDB = client["exhibition"]

    exhibitionDB["exhibitions"].insert_many(data)

    # 查詢集合內的全部資料
    print('所有展覽', exhibitionDB["exhibitions"].find())
