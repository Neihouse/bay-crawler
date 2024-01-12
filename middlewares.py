from scrapy import signals
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException

class SeleniumMiddleware:
    def __init__(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(executable_path='path/to/geckodriver', options=options)

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        self.driver.get(request.url)
        return HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=request)

    def spider_closed(self):
        self.driver.quit()