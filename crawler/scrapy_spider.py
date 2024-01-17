```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.utils import valid_url
from crawler.config import SEED_URLS, RATE_LIMIT

class EmailSpider(CrawlSpider):
    name = 'email_spider'
    allowed_domains = ['linkedin.com', 'yelp.com', 'facebook.com']
    start_urls = SEED_URLS
    download_delay = RATE_LIMIT

    rules = (
        Rule(LinkExtractor(allow_domains=allowed_domains), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if valid_url(response.url):
            yield {
                'url': response.url,
                'html': response.text,
            }
```
This code defines a Scrapy spider that starts from the seed URLs, follows links within the allowed domains, and yields the URL and HTML content of each page. The `valid_url` function (defined in `utils.py`) checks if a URL is within the 100-mile radius of the Bay Area. The rate limit is set to prevent overloading the servers of the websites being crawled. The yielded items will be processed by Scrapy's item pipeline, where the HTML content will be parsed to extract emails and other data.