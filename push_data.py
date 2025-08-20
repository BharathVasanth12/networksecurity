import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from dotenv import load_dotenv
from networksecurity.logging.logger import logger

#Initialize the loading env var
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

logger.info(f"Exporting MONGO_DB_URL:{MONGO_DB_URL}")

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json_converted(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongo_db(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == '__main__':
    FILE_PATH = 'network_data/phisingData.csv'
    DATABASE = 'networksecurity'
    Collection = 'NetworkData'
    networkDataExtractObj = NetworkDataExtract()
    records = networkDataExtractObj.csv_to_json_converted(file_path=FILE_PATH)
    print(f"Records:{records}")
    num_of_records = networkDataExtractObj.insert_data_mongo_db(records, DATABASE, Collection)

    print(f"Number of records:{num_of_records}")

        
