import pytest
from crawler.crawler import Crawler

def test_crawler_initialization():
    crawler = Crawler("http://example.com", 1)
    assert crawler.start_url == "http://example.com"
    assert crawler.depth == 1

# Additional tests to cover the crawler functionality