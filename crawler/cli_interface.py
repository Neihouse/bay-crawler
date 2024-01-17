```python
import argparse
from crawler.main import Crawler

def main():
    parser = argparse.ArgumentParser(description='Bay Area Email Crawler')
    parser.add_argument('-u', '--url', type=str, help='Seed URL to start crawling')
    parser.add_argument('-l', '--limit', type=int, default=100, help='Limit for number of pages to crawl')
    parser.add_argument('-r', '--rate', type=int, default=1, help='Rate limit for requests per second')
    parser.add_argument('-d', '--database', type=str, default='bigquery', help='Database to use for storage. Options: bigquery, mongodb')
    args = parser.parse_args()

    crawler = Crawler(seed_url=args.url, limit=args.limit, rate=args.rate, database=args.database)
    crawler.start()

if __name__ == "__main__":
    main()
```