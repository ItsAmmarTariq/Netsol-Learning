from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
