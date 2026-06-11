<<<<<<< HEAD
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)
=======
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:cyber2026@postgres:5432/fraud_detection_db"

engine = create_engine(DATABASE_URL)
>>>>>>> d7cc06efc5da1142cb42abd2819e93cfde5d83bb
