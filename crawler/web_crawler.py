import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self):
        self.base_url = 'http://example.com'

    def crawl(self):
        # Perform the web crawling logic here
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract data from the page
        data = self.extract_data(soup)
        return data

    def extract_data(self, soup):
        # Extract relevant data from the BeautifulSoup object
        # This is a placeholder for the actual data extraction logic
        return {'data': 'extracted data'}