from url_finder import URLFinder
import pytest

@pytest.fixture
def url_finder():
    return URLFinder()

def test_find_urls(url_finder):
    sample_html = "<a href='http://example.com'>Example</a>"
    urls = url_finder.find_urls(sample_html)
    assert "http://example.com" in urls