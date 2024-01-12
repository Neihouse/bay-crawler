import pytest
from storage.mongodb_client import MongoDBClient
from storage.bigquery_client import BigQueryClient

@pytest.fixture(scope="session")
def mongodb_client():
    return MongoDBClient()

@pytest.fixture(scope="session")
def bigquery_client():
    return BigQueryClient()