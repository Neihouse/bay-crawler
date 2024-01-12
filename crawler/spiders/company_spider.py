import scrapy
from crawler.items import ProductionCompanyItem
from crawler.utils import extract_emails

class CompanySpider(scrapy.Spider):
    name = 'company_spider'
    allowed_domains = ['example.com']  # Replace with actual allowed domains
    start_urls = ['http://www.example.com']  # Replace with actual start URLs

    def parse(self, response):
        item = ProductionCompanyItem()
        item['company_name'] = response.xpath('//h1/text()').get()
        item['email'] = extract_emails(response.text)
        item['source_url'] = response.url
        item['timestamp'] = datetime.now()
        yield item

        # Follow links to other company pages
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)