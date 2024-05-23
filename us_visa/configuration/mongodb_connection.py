import os
import sys
import pymongo
import certifi
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGO_DB_URL_KEY

ca = certifi.where()

class MongoDBClient:
    """
    Class name: export data into feature store
    Description: this feature export data from mongoDb to feature store
    Output: connection to Mongodb database
    Error: raise Exception
    """
    client = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(MONGO_DB_URL_KEY)
                if mongodb_url is None:
                    raise Exception(f"Environment Key:{MONGO_DB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDb Connection is Succesfull")
        except Exception as e:
            raise e