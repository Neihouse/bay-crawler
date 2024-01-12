from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

class UrlParser:
    def parse_urls(self, text):
        # Parse URLs from the given text
        soup = BeautifulSoup(text, 'html.parser')
        urls = [urljoin(base, link.get('href')) for link in soup.find_all('a', href=True)]
        return urls