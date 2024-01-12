from google.oauth2 import service_account
from google.cloud import storage, container_v1, compute_v1, bigquery

class GCPClient:
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
            'path/to/service-account-file.json'
        )
        self.storage_client = storage.Client(credentials=self.credentials)
        self.container_client = container_v1.ClusterManagerClient(credentials=self.credentials)
        self.compute_client = compute_v1.InstancesClient(credentials=self.credentials)
        self.bigquery_client = bigquery.Client(credentials=self.credentials)