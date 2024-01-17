```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SeleniumHandler:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(self.driver_path)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def load_page(self, url):
        self.driver.get(url)

    def wait_for_element(self, element_id, timeout=10):
        try:
            element_present = EC.presence_of_element_located((By.ID, element_id))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def get_page_source(self):
        return self.driver.page_source
```