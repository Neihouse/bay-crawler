from crawler import Crawler

class EmailCrawler(Crawler):
    def __init__(self, config):
        super().__init__(config)

    def crawl(self):
        # Implement email-specific crawling logic
        pass