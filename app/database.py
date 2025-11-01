from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

def get_database_url():
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        return database_url
    else:
        # Default to SQLite for local development
        return "sqlite:///./banking.db"

DATABASE_URL = get_database_url()

def create_database_engine():
    if DATABASE_URL.startswith("sqlite"):
        return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        return create_engine(DATABASE_URL, echo=False)

engine = create_database_engine()
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
