from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from crawler.models import Base

engine = create_engine('mysql+pymysql://user:password@localhost/dbname')  # Replace with actual DB credentials
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)