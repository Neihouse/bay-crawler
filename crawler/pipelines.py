from database_handler import DatabaseHandler

class EmailPipeline:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def process_item(self, item, spider):
        self.db_handler.save_item(dict(item))
        return item