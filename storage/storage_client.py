from google.cloud import storage

class StorageClient:
    def __init__(self):
        self.client = storage.Client()
        self.bucket_name = 'your-bucket-name'

    def save_data(self, data):
        # Save the data to the GCP Storage Bucket
        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob('data.json')
        blob.upload_from_string(data)