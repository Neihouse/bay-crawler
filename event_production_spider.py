import scrapy
from email_extractor import EmailExtractor
from items import EventProductionItem

class EventProductionSpider(scrapy.Spider):
    name = 'event_production_spider'
    allowed_domains = ['example.com']  # Replace with actual allowed domains
    start_urls = ['http://example.com']  # Replace with actual start URLs

    def parse(self, response):
        extractor = EmailExtractor()
        emails = extractor.extract_emails(response.text)
        for email in emails:
            item = EventProductionItem()
            item['email'] = email
            item['source_url'] = response.url
            yield item