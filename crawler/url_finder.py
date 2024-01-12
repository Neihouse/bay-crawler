from urllib.parse import urljoin
from bs4 import BeautifulSoup

class URLFinder:
    def find_urls(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return [urljoin(soup.base.get('href'), a.get('href')) for a in soup.find_all('a', href=True)]