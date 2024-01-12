from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class JavaScriptRenderer:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    def render(self, url):
        self.driver.get(url)
        page_source = self.driver.page_source
        self.driver.quit()
        return page_source
