class URLManager:
    def __init__(self):
        self.urls_to_crawl = set()
        self.crawled_urls = set()

    def add_url(self, url):
        if url not in self.crawled_urls:
            self.urls_to_crawl.add(url)

    def get_next_url(self):
        return self.urls_to_crawl.pop()

    def mark_as_crawled(self, url):
        self.crawled_urls.add(url)