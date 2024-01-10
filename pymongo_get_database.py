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

    exhibitionDB = client["exhibitions"]
    exhibitionCol = exhibitionDB["exhibitions"]
    print("Connected to MongoDB Atlas", exhibitionDB)
    print(client.list_database_names())
    client.close()


# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
    # Get the database
    # dbname = get_database()
get_database()
