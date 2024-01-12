import scrapy
from scrapy.crawler import CrawlerProcess

class BaseCrawler:
    def crawl(self):
        process = CrawlerProcess()
        process.crawl(MySpider)
        process.start()

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def start_requests(self):
        # Define the starting URLs for the crawler
        urls = ['http://example.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parsing logic goes here
        pass