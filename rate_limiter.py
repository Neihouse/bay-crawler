import time

class RateLimiter:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit
        self.last_call = time.time()

    def wait(self):
        elapsed_time = time.time() - self.last_call
        if elapsed_time < self.rate_limit:
            time.sleep(self.rate_limit - elapsed_time)
        self.last_call = time.time()