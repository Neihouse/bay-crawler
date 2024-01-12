from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventCompany(Base):
    __tablename__ = 'event_companies'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(255))
    email = Column(String(255))
    source_url = Column(String(255))
    timestamp = Column(DateTime)