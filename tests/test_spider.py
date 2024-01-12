import pytest
from scrapy.http import HtmlResponse
from crawler.spiders.company_spider import CompanySpider

def test_parse():
    spider = CompanySpider()
    html = """
    <html>
        <body>
            <h1>Test Company</h1>
            <a href="http://www.example.com/contact">Contact</a>
        </body>
    </html>
    """
    url = 'http://www.example.com'
    response = HtmlResponse(url=url, body=html.encode('utf-8'))
    parsed_items = list(spider.parse(response))

    assert len(parsed_items) == 1
    assert parsed_items[0]['company_name'] == 'Test Company'
    assert parsed_items[0]['source_url'] == url

def test_crawler_class():
    # Add tests for the Crawler class here
    pass