from threading import Timer
from logger import Logger
from crawler_settings import CrawlerSettings

class Scheduler:
    def __init__(self, settings: CrawlerSettings, logger: Logger):
        self.settings = settings
        self.logger = logger

    def schedule_crawl(self, url, crawl_function):
        Timer(0, crawl_function, [url]).start()