from crawler.crawler import Crawler

class EmailCrawler(Crawler):
    def __init__(self, config):
        super().__init__(config)

    def start(self):
        # Placeholder for specialized email crawling logic
        pass