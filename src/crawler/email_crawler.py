from .base_crawler import BaseCrawler

class EmailCrawler(BaseCrawler):
    def __init__(self, start_url, depth):
        super().__init__(start_url, depth)

    def get_spider(self):
        class EmailSpider(super().get_spider()):
            name = "email_spider"

            def parse(self, response):
                # Implement email-specific parsing logic here
                pass

        return EmailSpider