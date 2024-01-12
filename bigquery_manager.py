import google.auth
from google.cloud import bigquery

class BigqueryManager:
    def __init__(self):
        self.credentials, self.project = google.auth.default()

    # Add methods to interact with the respective GCP service here
