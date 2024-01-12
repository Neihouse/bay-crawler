from scrapy.crawler import CrawlerProcess
from crawler.spiders.example_spider import ExampleSpider

class Crawler:
    def __init__(self, config):
        self.config = config

    def start(self):
        process = CrawlerProcess(self.config)
        process.crawl(ExampleSpider)
        process.start()