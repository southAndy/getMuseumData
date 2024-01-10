from pymongo import MongoClient
# 引入環境變數
from dotenv import load_dotenv
import os


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    load_dotenv()
    database_url = os.getenv('DB_URL_LOCAL')
    CONNECTION_STRING = database_url

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # 切換到展覽資料庫
    exhibitionDB = client["exhibition"]

    # 新增一筆展覽資料
    exhibitionDB["exhibitions"].insert_one(
        {"title": "台北美術館大展", "description": "test"})

    # 查詢資料庫內的集合
    print(exhibitionDB.list_collection_names())

    # 查詢集合內的全部資料
    print('所有展覽', exhibitionDB["exhibitions"].find())


get_database()
