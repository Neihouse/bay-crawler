from bs4 import BeautifulSoup

class HTMLParser:
    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Parsing logic goes here
        return soup