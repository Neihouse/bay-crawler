import requests
from bs4 import BeautifulSoup

class PageFetcher:
    def fetch(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def extract_urls(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]