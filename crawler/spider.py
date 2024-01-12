import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    
    def start_requests(self):
        # Define the starting URLs for the crawler
        urls = ['http://example.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # Parsing logic using BeautifulSoup or other methods
        pass