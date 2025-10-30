from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

def get_database_url():
    """Get database URL based on environment configuration"""
    database_url = os.getenv("DATABASE_URL")
    
    if database_url:
        return database_url
    else:
        # Default to SQLite for local development
        return "sqlite:///./banking.db"

DATABASE_URL = get_database_url()

def create_database_engine():
    """Create database engine with appropriate configuration"""
    if DATABASE_URL.startswith("sqlite"):
        # SQLite specific configuration
        return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    else:
        # PostgreSQL configuration
        return create_engine(DATABASE_URL, echo=False)

engine = create_database_engine()
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
