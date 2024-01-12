import re

class EmailCrawler:
    def extract_emails(self, data):
        # Logic to extract emails from the data
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
        self.store_emails(emails)

    def store_emails(self, emails):
        # Logic to store emails
        pass