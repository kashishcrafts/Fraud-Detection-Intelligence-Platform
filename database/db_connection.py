<<<<<<< HEAD
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/fraud_detection_db"

engine = create_engine(DATABASE_URL)

=======
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/fraud_detection_db"

engine = create_engine(DATABASE_URL)

>>>>>>> d7cc06efc5da1142cb42abd2819e93cfde5d83bb
print("Database Connected Successfully")