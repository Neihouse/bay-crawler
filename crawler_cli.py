from email_crawler import EmailCrawler

class CrawlerCLI:
    def run(self):
        crawler = EmailCrawler()
        crawler.start_crawl()