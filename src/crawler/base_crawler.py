import scrapy
from scrapy.crawler import CrawlerProcess

class BaseCrawler:
    def __init__(self, start_url, depth):
        self.start_url = start_url
        self.depth = depth

    def start(self):
        process = CrawlerProcess()
        process.crawl(self.get_spider())
        process.start()

    def get_spider(self):
        class Spider(scrapy.Spider):
            name = "base_spider"
            allowed_domains = [self.get_domain()]
            start_urls = [self.start_url]

            def parse(self, response):
                # Implement parsing logic here
                pass

        return Spider

    def get_domain(self):
        # Extract domain from start_url
        pass