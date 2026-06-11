<<<<<<< HEAD
from fastapi import FastAPI, Header
import joblib
from pydantic import BaseModel

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Float,
    DateTime,
    String,
    insert,
    select
)

from datetime import datetime

from database.db import engine

from backend.auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

app = FastAPI()

# Load ML Model
model = joblib.load("models/random_forest.pkl")

# ==========================
# Database Tables
# ==========================

metadata = MetaData()

predictions_table = Table(
    "predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("prediction", Integer, nullable=False),
    Column("fraud_probability", Float),
    Column("username", String(100)),
    Column("created_at", DateTime, default=datetime.utcnow)
)

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100), unique=True, nullable=False),
    Column("password", String(255), nullable=False)
)

metadata.create_all(engine)

# ==========================
# Request Schemas
# ==========================

class Transaction(BaseModel):
    features: list[float]


class BatchTransactions(BaseModel):
    transactions: list[list[float]]


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# ==========================
# Routes
# ==========================

@app.get("/")
def home():
    return {
        "message": "Fraud Detection Intelligence Platform API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ==========================
# Register
# ==========================

@app.post("/register")
def register(user: RegisterRequest):

    hashed_password = hash_password(
        user.password
    )

    stmt = insert(users_table).values(
        username=user.username,
        password=hashed_password
    )

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return {
        "message": "User registered successfully"
    }


# ==========================
# Login
# ==========================

@app.post("/login")
def login(user: LoginRequest):

    with engine.connect() as conn:

        result = conn.execute(
            select(users_table).where(
                users_table.c.username == user.username
            )
        )

        db_user = result.fetchone()

    if not db_user:
        return {
            "error": "Invalid username"
        }

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {
            "error": "Invalid password"
        }

    token = create_access_token(
        {
            "sub": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ==========================
# Single Prediction
# ==========================

@app.post("/predict")
def predict(
    transaction: Transaction,
    authorization: str = Header(None)
):

    if not authorization:
        return {
            "error": "Authorization token required"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    username = verify_token(token)

    if not username:
        return {
            "error": "Invalid token"
        }

    prediction = model.predict(
        [transaction.features]
    )

    probability = model.predict_proba(
        [transaction.features]
    )

    fraud_probability = float(
        probability[0][1]
    )

    stmt = insert(predictions_table).values(
    prediction=int(prediction[0]),
    fraud_probability=fraud_probability,
    username=username
)

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return {
        "prediction": int(prediction[0]),
        "fraud_probability": round(
            fraud_probability * 100,
            2
        )
    }


# ==========================
# Batch Prediction
# ==========================

@app.post("/predict-batch")
def predict_batch(
    data: BatchTransactions,
    authorization: str = Header(None)
):
    if not authorization:
        return {
            "error": "Authorization token required"
        }

    token = authorization.replace(
        "Bearer ",
     ""
    )

    username = verify_token(token)

    if not username:
        return {
            "error": "Invalid token"
        }

    predictions = model.predict(
        data.transactions
    )

    fraud_probabilities = model.predict_proba(
        data.transactions
    )[:, 1]

    return {
        "predictions": predictions.tolist(),
        "fraud_probabilities": fraud_probabilities.tolist()
    }


# ==========================
# Prediction History
# ==========================

@app.get("/predictions")
def get_predictions(
    authorization: str = Header(None)
):
    
    if not authorization:
        return {
            "error": "Authorization token required"
        }

        token = authorization.replace(
            "Bearer ",
            ""
        )

        username = verify_token(token)

    if not username:
        return {
            "error": "Invalid token"
       }    

    with engine.connect() as conn:

        result = conn.execute(
    select(predictions_table).where(
        predictions_table.c.username == username
    )
)

        data = [
            dict(row._mapping)
            for row in result
        ]

=======
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

>>>>>>> d7cc06efc5da1142cb42abd2819e93cfde5d83bb
    return data