import requests
from src.parser import Parser

class Crawler:
    def __init__(self, config, url_manager):
        self.config = config
        self.url_manager = url_manager
        self.parser = Parser()

    def crawl(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return self.parser.parse(response.text)
        else:
            # Handle non-successful HTTP responses
            return None