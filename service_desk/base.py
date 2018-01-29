from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
# engine = create_engine('postgresql://usr:pass@localhost:5432/servicedesk')
Session = sessionmaker(bind=engine)

Base = declarative_base()
