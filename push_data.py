import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

"""
This module handles data extraction and ingestion for the Network Security project.
It is responsible for loading environment variables, reading CSV data files,
transforming them into JSON-compatible records, and inserting the processed data
into a MongoDB database.

The `NetworkdataExtract` class provides methods to convert CSV files into JSON
records and persist them into a specified MongoDB collection while ensuring
robust exception handling and logging using custom exceptions.

Args:
    file_path (_type_): Path to the CSV file containing network security data.
    records (_type_): List of JSON-like records derived from the CSV file.
    database (_type_): Name of the MongoDB database.
    collection (_type_): Name of the MongoDB collection.

Returns:
    _type_: Number of records successfully inserted into the MongoDB collection.
"""


class NetworkdataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convert(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.transpose().to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
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
        
if __name__ == "__main__":
    FILE_PATH = "C:/Users/DJ668WN/Downloads/NetworkSecurity/Network_Data/phisingData.csv"
    DATABASE = "RAHUL"
    Collection = "NetworkData"
    network_obj = NetworkdataExtract()
    records = network_obj.csv_to_json_convert(file_path=FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_mongodb(records=records, database=DATABASE, collection=Collection)
    print(no_of_records)