```python
from pymongo import MongoClient
from crawler.config import MONGODB_URI, MONGODB_DB, MONGODB_COLLECTION

class MongoDBHandler:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[MONGODB_DB]
        self.collection = self.db[MONGODB_COLLECTION]

    def insert_data(self, data):
        self.collection.insert_one(data)

    def get_data(self, query):
        return self.collection.find(query)

    def update_data(self, query, new_data):
        self.collection.update_one(query, {"$set": new_data})

    def delete_data(self, query):
        self.collection.delete_one(query)
```