from url_manager import URLManager
from parser import Parser
from storage import Storage

class Crawler:
    def __init__(self, config):
        self.config = config
        self.url_manager = URLManager(config.start_urls, config.allowed_domains)
        self.parser = Parser()
        self.storage = Storage()

    def crawl(self):
        # Implement the crawling logic
        pass