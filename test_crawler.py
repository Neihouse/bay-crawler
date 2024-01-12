import pytest
from crawler import Crawler
from config import Config

def test_crawler_initialization():
    config = Config()
    crawler = Crawler(config)
    assert crawler is not None

# Add more tests as needed