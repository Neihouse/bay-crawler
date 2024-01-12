import scrapy
from email_crawler.items import EmailItem
from email_crawler.utils import extract_emails, handle_javascript_content
from scrapy.http import Request

class EventProductionSpider(scrapy.Spider):
    name = 'event_production'
    allowed_domains = ['example.com']  # Replace with actual allowed domains
    start_urls = ['http://example.com']  # Replace with actual start URLs

    def parse(self, response):
        # Extract emails from the page
        emails = extract_emails(response.text)
        for email in emails:
            yield EmailItem(email=email, source_url=response.url)

        # Follow links to other pages
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)

        # Handle JavaScript content if necessary
        if 'javascript' in response.headers.get('Content-Type', '').decode('utf-8'):
            yield Request(response.url, callback=self.parse_js, dont_filter=True)

    def parse_js(self, response):
        # Use Selenium to handle JavaScript content
        html = handle_javascript_content(response.url)
        return self.parse(html)