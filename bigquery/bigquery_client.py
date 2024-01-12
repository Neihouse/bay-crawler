from google.cloud import bigquery

class BigQueryClient:
    def __init__(self):
        self.client = bigquery.Client()
        self.dataset_id = 'your_dataset_id'
        self.table_id = 'your_table_id'

    def insert_data(self, data):
        # Insert the data into BigQuery
        dataset_ref = self.client.dataset(self.dataset_id)
        table_ref = dataset_ref.table(self.table_id)
        table = self.client.get_table(table_ref)
        # This is a placeholder for the actual data insertion logic
        self.client.insert_rows_json(table, [data])