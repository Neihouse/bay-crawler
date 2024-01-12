import re
from bs4 import BeautifulSoup

def parse_emails(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails