from sqlalchemy.orm import sessionmaker
from email_crawler.models import db_connect, create_table, Email
from scrapy.exceptions import DropItem

class EmailPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save emails in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        email = Email(**item)

        try:
            session.add(email)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item