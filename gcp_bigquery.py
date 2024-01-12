from google.cloud import bigquery

class BigQueryClient:
    def __init__(self):
        self.client = bigquery.Client()

    def create_dataset(self, dataset_id):
        """Create a new BigQuery dataset."""
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        created_dataset = self.client.create_dataset(dataset, timeout=30)
        print(f"Created dataset {created_dataset.dataset_id}")

    def create_table(self, table_id):
        """Create a new BigQuery table."""
        # This is a simplified example. In practice, you would need to define
        # a schema for the table.
        schema = [
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("value", "FLOAT", mode="REQUIRED"),
        ]
        table = bigquery.Table(table_id, schema=schema)
        created_table = self.client.create_table(table)
        print(f"Created table {created_table.table_id}")

    def query_data(self, query):
        """Run a query on BigQuery tables."""
        query_job = self.client.query(query)
        results = query_job.result()
        for row in results:
            print(f"{row.name}: {row.value}")