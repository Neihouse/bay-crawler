import requests
from urllib.parse import urlparse

def is_allowed_to_crawl(url):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    response = requests.get(robots_url)
    if response.status_code == 200:
        # Implement logic to parse robots.txt and determine if crawling is allowed
        return True
    return False