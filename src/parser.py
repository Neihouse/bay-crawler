from bs4 import BeautifulSoup

class Parser:
    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract data from the HTML content using BeautifulSoup
        data = {}
        # Populate the data dictionary with extracted information
        return data