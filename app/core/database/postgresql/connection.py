from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
import logging

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.postgres_db_user}:{settings.postgres_db_password}@{settings.postgres_db_host}/{settings.postgres_db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        yield db
    except Exception as e:
      logging.error(f"Error connecting to DB: {e}")
      raise e
    finally:
      logging.info("Closing DB connection...")
      db.close()