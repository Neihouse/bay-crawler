```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from cli_interface import CLIInterface
from config import Config
from utils import load_seed_urls

def main():
    # Initialize CLI Interface
    cli = CLIInterface()
    config = Config()

    # Load configuration from CLI
    config.load_from_cli(cli)

    # Load seed URLs
    seed_urls = load_seed_urls(config.seed_url_file)

    # Initialize Scrapy settings
    settings = get_project_settings()
    settings.set('SEED_URLS', seed_urls)
    settings.set('RATE_LIMIT', config.rate_limit)
    settings.set('BIGQUERY_PROJECT_ID', config.bigquery_project_id)
    settings.set('MONGODB_URI', config.mongodb_uri)

    # Initialize Scrapy process
    process = CrawlerProcess(settings)

    # Start the crawler with the scrapy spider
    process.crawl('scrapy_spider')
    process.start()

if __name__ == "__main__":
    main()
```