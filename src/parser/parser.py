from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extract_data(self):
        # Implement data extraction logic here
        pass