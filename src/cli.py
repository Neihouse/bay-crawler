import argparse
from src.crawler.email_crawler import EmailCrawler

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Bay Area Production Company Email Crawler")
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument('--start', help='Start the crawler', action='store_true')
        self.parser.add_argument('--url', help='Seed URL to start crawling from', type=str)

    def run(self):
        args = self.parser.parse_args()
        if args.start:
            crawler = EmailCrawler(seed_url=args.url)
            crawler.start_crawling()