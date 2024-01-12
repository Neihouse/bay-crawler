from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options

class SeleniumMiddleware:
    def process_request(self, request, spider):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(request.url)
        body = driver.page_source
        driver.quit()
        return HtmlResponse(request.url, body=body, encoding='utf-8', request=request)