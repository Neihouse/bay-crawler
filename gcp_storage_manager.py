from google.cloud import storage

class GCPStorageManager:
    def __init__(self):
        self.client = storage.Client()

    def create_bucket(self, bucket_name):
        bucket = self.client.bucket(bucket_name)
        new_bucket = self.client.create_bucket(bucket)
        print(f"Bucket {new_bucket.name} created.")