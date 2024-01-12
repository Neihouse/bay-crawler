import re

class EmailExtractor:
    def extract_emails(self, text):
        # Regular expression for extracting emails
        email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        return email_regex.findall(text)