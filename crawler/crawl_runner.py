from .email_crawler import EmailCrawler
from .proxy_manager import ProxyManager
from .storage_manager import StorageManager
from .scheduler import Scheduler
from .logger import Logger

class CrawlRunner:
    def __init__(self):
        self.logger = Logger()
        self.proxy_manager = ProxyManager(self.logger)
        self.storage_manager = StorageManager(self.logger)
        self.scheduler = Scheduler(self.logger)
        self.email_crawler = EmailCrawler(self.proxy_manager, self.storage_manager, self.logger)

    def run(self):
        # Start the crawling process
        self.scheduler.schedule(self.email_crawler.start)