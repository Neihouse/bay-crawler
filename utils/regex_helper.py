import re

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

def extract_emails(text):
    return EMAIL_REGEX.findall(text)