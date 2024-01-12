from sqlalchemy.orm import sessionmaker
from models import EventProductionEmail, db_connect, create_table

class EventProductionPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        email = EventProductionEmail(**item)
        session.add(email)
        session.commit()
        session.close()
        return item