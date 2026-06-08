# 🛡️ Fraud Detection Intelligence Platform

An end-to-end AI-powered Fraud Detection Intelligence Platform built using Machine Learning, FastAPI, PostgreSQL, Streamlit, and Docker.

## 🚀 Features

* Fraud Detection using Random Forest Classifier
* FastAPI REST API
* Batch Prediction API
* Prediction History Tracking
* PostgreSQL Database Integration
* Interactive Streamlit Dashboard
* CSV Upload & Analysis
* Fraud vs Genuine Visualization
* Dockerized Multi-Container Deployment

## 🏗️ Architecture

![Architecture Diagram](docs/architecture_diagram.png)

## 📊 Dashboard Features

* Upload Transaction Dataset
* Detect Fraudulent Transactions
* View Fraud Statistics
* Interactive Charts
* Download Prediction Results
* Prediction History

## 🛠️ Tech Stack

* Python
* Scikit-Learn
* FastAPI
* Streamlit
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose

## 📂 Project Structure

```text
Fraud-Detection-Intelligence-Platform/
│
├── backend/
├── database/
├── models/
├── docs/
├── screenshots/
├── app.py
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## ⚙️ Running with Docker

```bash
docker compose up --build
```

### Services

* Streamlit Dashboard → http://localhost:8501
* FastAPI Backend → http://localhost:8000
* Swagger Docs → http://localhost:8000/docs
* PostgreSQL → Port 5432

## 🔮 Future Enhancements

* Real-time Fraud Detection
* Kafka Streaming Pipeline
* Cloud Deployment
* Advanced ML Models
* Monitoring & Logging

## 👩‍💻 Author

Kashish Shaikh

Computer Engineering Student | AI/ML | Data Engineering | Cybersecurity

