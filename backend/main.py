from fastapi import FastAPI
import joblib
from pydantic import BaseModel
from sqlalchemy import MetaData, Table, insert
from database.db import engine

app = FastAPI()

# Load ML Model
model = joblib.load("models/random_forest.pkl")

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Float,
    DateTime
)
from datetime import datetime

metadata = MetaData()

predictions_table = Table(
    "predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("prediction", Integer, nullable=False),
    Column("fraud_probability", Float),
    Column("created_at", DateTime, default=datetime.utcnow)
)

metadata.create_all(engine)

# Request Schemas
class Transaction(BaseModel):
    features: list[float]

class BatchTransactions(BaseModel):
    transactions: list[list[float]]

# Home Route
@app.get("/")
def home():
    return {
        "message": "Fraud Detection Intelligence Platform API Running"
    }

# Single Prediction Route
@app.post("/predict")
def predict(transaction: Transaction):

    prediction = model.predict(
        [transaction.features]
    )

    # Save Prediction to PostgreSQL
    stmt = insert(predictions_table).values(
        prediction=int(prediction[0]),
        fraud_probability=0.0
    )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return {
        "prediction": int(prediction[0])
    }

# Batch Prediction Route
@app.post("/predict-batch")
def predict_batch(data: BatchTransactions):

    predictions = model.predict(
        data.transactions
    )

    return {
        "predictions": predictions.tolist()
    }

from sqlalchemy import select

@app.get("/predictions")
def get_predictions():

    with engine.connect() as conn:
        result = conn.execute(
            select(predictions_table)
        )

        data = [
            dict(row._mapping)
            for row in result
        ]

    return data