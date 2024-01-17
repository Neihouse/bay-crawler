```python
# crawler/config.py

# Importing required libraries
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Seed URLs
SEED_URLS = [
    'https://www.linkedin.com/',
    'https://www.yelp.com/',
    'https://www.facebook.com/'
]

# Rate limiting parameters
RATE_LIMIT = 10  # Number of requests per minute

# Database connection details
BIGQUERY_CONNECTION_DETAILS = {
    'project_id': os.getenv('BIGQUERY_PROJECT_ID'),
    'dataset_id': os.getenv('BIGQUERY_DATASET_ID'),
    'table_id': os.getenv('BIGQUERY_TABLE_ID'),
    'credentials_path': os.getenv('BIGQUERY_CREDENTIALS_PATH')
}

MONGODB_CONNECTION_DETAILS = {
    'host': os.getenv('MONGODB_HOST'),
    'port': os.getenv('MONGODB_PORT'),
    'database': os.getenv('MONGODB_DATABASE'),
    'collection': os.getenv('MONGODB_COLLECTION')
}

# Data schema
DATA_SCHEMA = ['company_name', 'email', 'source_url', 'timestamp']

# Regular expression for email extraction
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# DOM element IDs
DOM_ELEMENT_IDS = {
    'linkedin': 'ember52',
    'yelp': 'yelp-react-root',
    'facebook': 'mount_0_0'
}

# Message names
MESSAGE_NAMES = {
    'start_crawl': 'Starting the crawl...',
    'end_crawl': 'Crawl completed successfully.',
    'error_crawl': 'An error occurred during the crawl.'
}
```