from pymongo import MongoClient
from google.cloud import bigquery

class DatabaseManager:
    def __init__(self):
        self.mongo_client = MongoClient()
        self.mongo_db = self.mongo_client.email_crawler
        self.mongo_collection = self.mongo_db.emails
        self.bigquery_client = bigquery.Client()

    def store_emails(self, emails, source_url):
        for email in emails:
            self.mongo_collection.insert_one({'email': email, 'source_url': source_url})
            # Additional code to store data in Google BigQuery would go here