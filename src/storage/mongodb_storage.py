from pymongo import MongoClient

class MongoDBStorage:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.bay_crawler

    def store_data(self, data):
        # Method to store data in MongoDB
        pass