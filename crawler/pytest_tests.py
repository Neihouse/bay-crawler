```python
import pytest
from crawler import main, scrapy_spider, beautifulsoup_parser, selenium_handler, pandas_data_manipulation, regex_email_extractor, bigquery_handler, mongodb_handler

def test_scrapy_spider():
    assert scrapy_spider.crawl() is not None, "Scrapy spider failed to crawl"

def test_beautifulsoup_parser():
    html_content = "<html><body><p>Test</p></body></html>"
    assert beautifulsoup_parser.parse(html_content) is not None, "BeautifulSoup failed to parse HTML"

def test_selenium_handler():
    assert selenium_handler.handle_js() is not None, "Selenium failed to handle JavaScript content"

def test_pandas_data_manipulation():
    data = {"Company": ["Test"], "Email": ["test@test.com"], "Source URL": ["http://test.com"], "Timestamp": ["2022-01-01 00:00:00"]}
    assert pandas_data_manipulation.manipulate(data) is not None, "Pandas failed to manipulate data"

def test_regex_email_extractor():
    text = "test@test.com"
    assert regex_email_extractor.extract(text) == ["test@test.com"], "Regex failed to extract email"

def test_bigquery_handler():
    data = {"Company": ["Test"], "Email": ["test@test.com"], "Source URL": ["http://test.com"], "Timestamp": ["2022-01-01 00:00:00"]}
    assert bigquery_handler.store(data) is not None, "BigQuery failed to store data"

def test_mongodb_handler():
    data = {"Company": "Test", "Email": "test@test.com", "Source URL": "http://test.com", "Timestamp": "2022-01-01 00:00:00"}
    assert mongodb_handler.store(data) is not None, "MongoDB failed to store data"

if __name__ == "__main__":
    pytest.main()
```