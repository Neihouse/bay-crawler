from google.cloud import storage

class StorageClient:
    def __init__(self):
        self.client = storage.Client()

    def create_bucket(self, bucket_name):
        """Create a new storage bucket."""
        bucket = self.client.bucket(bucket_name)
        new_bucket = self.client.create_bucket(bucket)
        print(f"Bucket {new_bucket.name} created.")

    def upload_file(self, bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    def download_file(self, bucket_name, source_blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")