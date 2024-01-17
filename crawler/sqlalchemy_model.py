```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    source_url = Column(String)
    timestamp = Column(DateTime)

    def __init__(self, name, email, source_url, timestamp):
        self.name = name
        self.email = email
        self.source_url = source_url
        self.timestamp = timestamp

    def __repr__(self):
        return "<Company(name='%s', email='%s', source_url='%s', timestamp='%s')>" % (
            self.name, self.email, self.source_url, self.timestamp)
```