class CrawlerSettings:
    def __init__(self):
        self.user_agent = "Bay Area Event Production Crawler"
        self.proxy_list = "proxies.txt"
        self.database_uri = "mysql+pymysql://user:password@localhost:3306/crawler_db"
        # Additional settings can be added here