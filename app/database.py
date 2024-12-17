from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL="sqlite:///./kitchen.db"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./kitchen.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
