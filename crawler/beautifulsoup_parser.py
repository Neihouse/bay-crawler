```python
from bs4 import BeautifulSoup
from crawler.regex_email_extractor import extract_emails
from crawler.utils import get_html_content

class BeautifulSoupParser:
    def __init__(self):
        self.soup = None

    def load_html(self, url):
        html_content = get_html_content(url)
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def get_emails(self):
        if self.soup:
            return extract_emails(str(self.soup))
        else:
            return []

    def get_links(self):
        if self.soup:
            return [a['href'] for a in self.soup.find_all('a', href=True)]
        else:
            return []
```