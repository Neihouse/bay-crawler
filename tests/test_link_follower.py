from link_follower import LinkFollower
import pytest

def test_follow():
    follower = LinkFollower()
    content = "<a href='http://example.com'>Example</a>"
    links = follower.follow(content)
    assert "http://example.com" in links

def test_url_acquisition():
    acquisition = URLAcquisition()
    seed_urls = acquisition.get_seed_urls()
    assert isinstance(seed_urls, list)
    assert all(isinstance(url, str) for url in seed_urls)