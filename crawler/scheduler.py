import time

class Scheduler:
    def __init__(self, logger):
        self.logger = logger

    def schedule(self, task):
        # Schedule tasks to be run
        # This is a placeholder for the actual scheduling logic
        while True:
            task()
            time.sleep(10)  # Wait for 10 seconds before the next task