from sqlalchemy.orm import declarative_base, sessionmaker, registry
from sqlalchemy import create_engine

# Database URL
db_url = "sqlite:///cli-journal.db"

# Create the SQLAlchemy engine
engine = create_engine(db_url)

Base = declarative_base()

Base.metadata.bind = engine
    
# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()
