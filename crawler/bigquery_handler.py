```python
from google.cloud import bigquery
from crawler.config import BIGQUERY_PROJECT_ID, BIGQUERY_DATASET_ID, BIGQUERY_TABLE_ID

class BigQueryHandler:
    def __init__(self):
        self.client = bigquery.Client(project=BIGQUERY_PROJECT_ID)
        self.dataset_ref = self.client.dataset(BIGQUERY_DATASET_ID)
        self.table_ref = self.dataset_ref.table(BIGQUERY_TABLE_ID)

    def insert_data(self, data):
        table = self.client.get_table(self.table_ref)
        rows_to_insert = [data]
        errors = self.client.insert_rows(table, rows_to_insert)
        if errors:
            print(f'Encountered errors while inserting rows: {errors}')
        else:
            print('Rows inserted successfully.')

    def query_data(self, query):
        query_job = self.client.query(query)
        return query_job.result()
```