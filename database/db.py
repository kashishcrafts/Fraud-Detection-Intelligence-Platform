from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:cyber2026@postgres:5432/fraud_detection_db"

engine = create_engine(DATABASE_URL)