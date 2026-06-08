# Fraud Detection Intelligence Platform - Architecture Diagram

```text
┌─────────────────────────────────────────────┐
│                   USER                      │
│      Upload Transaction CSV Dataset         │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│              STREAMLIT UI                   │
│---------------------------------------------│
│ • Upload CSV                                │
│ • View Predictions                          │
│ • Fraud Analytics Dashboard                 │
│ • Prediction History                        │
│ • Download Results                          │
└──────────────────┬──────────────────────────┘
                   │ REST API Calls
                   ▼
┌─────────────────────────────────────────────┐
│                 FASTAPI                     │
│---------------------------------------------│
│ /predict                                    │
│ /predict-batch                              │
│ /predictions                                │
└───────────────┬───────────────┬─────────────┘
                │               │
                │               │
                ▼               ▼
┌──────────────────────┐   ┌──────────────────┐
│  Random Forest Model │   │ PostgreSQL DB    │
│----------------------│   │------------------│
│ Fraud Classification │   │ Prediction Logs  │
│ ML Inference Engine  │   │ History Storage  │
└──────────────────────┘   └──────────────────┘


====================================================

Docker Architecture

┌─────────────────────────────────────────────┐
│              Docker Network                 │
│                                             │
│  ┌───────────────┐                          │
│  │ fraud_streamlit│                         │
│  │ Port: 8501    │                          │
│  └───────┬───────┘                          │
│          │ HTTP                             │
│          ▼                                  │
│  ┌───────────────┐                          │
│  │ fraud_fastapi │                          │
│  │ Port: 8000    │                          │
│  └───────┬───────┘                          │
│          │ SQLAlchemy                       │
│          ▼                                  │
│  ┌───────────────┐                          │
│  │ fraud_postgres│                          │
│  │ Port: 5432    │                          │
│  └───────────────┘                          │
│                                             │
└─────────────────────────────────────────────┘
```

## Technology Stack

* Frontend: Streamlit
* Backend: FastAPI
* Database: PostgreSQL
* Machine Learning: Random Forest Classifier
* Containerization: Docker
* Orchestration: Docker Compose

## Data Flow

1. User uploads transaction CSV.
2. Streamlit sends transaction data to FastAPI.
3. FastAPI loads Random Forest model.
4. Model predicts Fraud / Genuine transaction.
5. Prediction stored in PostgreSQL.
6. FastAPI returns results.
7. Streamlit displays analytics dashboard.
8. User downloads prediction results.
9. History endpoint retrieves previous predictions.

```
```
