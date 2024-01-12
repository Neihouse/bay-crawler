import requests
from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    def __init__(self, start_url, depth):
        self.start_url = start_url
        self.depth = depth
        self.visited_urls = set()
    
    @abstractmethod
    def parse(self, html):
        pass
    
    def crawl(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)
        response = requests.get(url, headers={'User-Agent': config.USER_AGENT})
        self.parse(response.text)
    
    def start_crawling(self):
        self.crawl(self.start_url)