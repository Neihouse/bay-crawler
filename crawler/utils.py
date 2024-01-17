```python
import re
import datetime
from urllib.parse import urlparse

def extract_domain(url):
    """
    Extracts domain from a given URL
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

def validate_email(email):
    """
    Validates if a given string is a valid email address
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(email_regex, email):
        return True
    return False

def get_current_timestamp():
    """
    Returns the current timestamp
    """
    return datetime.datetime.now()

def handle_rate_limiting(delay):
    """
    Handles rate limiting by introducing delay
    """
    time.sleep(delay)
```