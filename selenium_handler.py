from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumHandler:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    def get_dynamic_content(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.quit()