import pymongo
from premium.Constant.database import DATABASE_NAME,MONGODB_URL
from premium.util.util import read_yaml_file
import certifi
import os
ca = certifi.where()

MONGODB_URL_KEY = "MONGO_DB_URL"
class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db = read_yaml_file(file_path='/Config/mongo.yaml')
                mongo_db_url = mongo_db[MONGODB_URL]
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e


