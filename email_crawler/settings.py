BOT_NAME = 'email_crawler'

SPIDER_MODULES = ['email_crawler.spiders']
NEWSPIDER_MODULE = 'email_crawler.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'email_crawler.pipelines.EmailPipeline': 300,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
   'email_crawler.middlewares.EmailCrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
   'email_crawler.middlewares.EmailCrawlerDownloaderMiddleware': 543,
}

# Enable or disable extensions
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'email_crawler.pipelines.EmailPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Enable showing crawling stats for every response received:
STATS_DUMP = True