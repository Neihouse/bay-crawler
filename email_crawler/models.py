from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import datetime
import email_crawler.settings as settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Email(DeclarativeBase):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    email = Column('email', String, nullable=False)
    source_url = Column('source_url', String, nullable=False)
    timestamp = Column('timestamp', DateTime, default=datetime.datetime.utcnow)