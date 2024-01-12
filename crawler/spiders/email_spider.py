import scrapy
from crawler.items import EmailItem
from crawler.email_extractor import EmailExtractor
from crawler.url_finder import URLFinder

class EmailSpider(scrapy.Spider):
    name = 'email_spider'

    def __init__(self, db_handler, proxy_manager, options, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)
        self.db_handler = db_handler
        self.proxy_manager = proxy_manager
        self.options = options
        self.start_urls = options.start_urls
        self.email_extractor = EmailExtractor()
        self.url_finder = URLFinder()

    def parse(self, response):
        emails = self.email_extractor.extract_emails(response.text)
        for email in emails:
            yield EmailItem(email=email, source_url=response.url)

        for url in self.url_finder.find_urls(response.text):
            yield scrapy.Request(url, callback=self.parse)