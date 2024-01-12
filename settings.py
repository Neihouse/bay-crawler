import os
import json

class Settings:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        # Load settings from a JSON file or environment variables
        return json.loads(os.getenv('CRAWLER_CONFIG', '{}'))

    def get_seed_urls(self):
        return self.config.get('seed_urls', [])