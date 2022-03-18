from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
SessionLocal: sessionmaker = sessionmaker(autoflush=True, autocommit=True, bind=engine)