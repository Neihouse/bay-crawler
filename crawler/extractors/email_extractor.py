import re

class EmailExtractor:
    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    def extract_emails(self, text):
        return re.findall(self.EMAIL_REGEX, text)