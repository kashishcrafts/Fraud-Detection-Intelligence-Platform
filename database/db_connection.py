from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/fraud_detection_db"

engine = create_engine(DATABASE_URL)

print("Database Connected Successfully")