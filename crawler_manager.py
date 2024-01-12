from scrapy.crawler import CrawlerProcess
from crawler.spiders.email_spider import EmailSpider
from database_handler import DatabaseHandler
from proxy_manager import ProxyManager

class CrawlerManager:
    def __init__(self, options):
        self.options = options
        self.db_handler = DatabaseHandler()
        self.proxy_manager = ProxyManager()
        self.crawler_process = CrawlerProcess({
            'DOWNLOADER_MIDDLEWARES': {
                'crawler.middlewares.SeleniumMiddleware': 800,
            }
        })

    def start_crawling(self):
        self.crawler_process.crawl(EmailSpider, db_handler=self.db_handler, proxy_manager=self.proxy_manager, options=self.options)
        self.crawler_process.start()