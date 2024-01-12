from src.crawlers.base_crawler import BaseCrawler

class CrawlerManager:
    def __init__(self):
        self.crawler = BaseCrawler()

    def start_crawling(self):
        self.crawler.crawl()