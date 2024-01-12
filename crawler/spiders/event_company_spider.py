import scrapy
from crawler.items import EventCompanyItem
from utils.email_extractor import extract_emails

class EventCompanySpider(scrapy.Spider):
    name = 'event_company'
    allowed_domains = ['example.com']  # Replace with actual domain names
    start_urls = ['http://www.example.com']  # Replace with actual start URLs

    def parse(self, response):
        item = EventCompanyItem()
        item['company_name'] = response.xpath('//title/text()').get()
        item['email'] = extract_emails(response.text)
        item['source_url'] = response.url
        item['timestamp'] = datetime.now()
        yield item

        # Follow links to other company pages (if any)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)