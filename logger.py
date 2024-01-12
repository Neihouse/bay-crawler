import logging

class Logger:
    @staticmethod
    def log(message, level=logging.INFO):
        logging.log(level, message)