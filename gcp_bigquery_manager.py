from google.cloud import bigquery

class GCPBigQueryManager:
    def __init__(self):
        self.client = bigquery.Client()

    def create_dataset(self, dataset_id):
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        dataset = self.client.create_dataset(dataset)
        print(f"Dataset {dataset.dataset_id} created.")