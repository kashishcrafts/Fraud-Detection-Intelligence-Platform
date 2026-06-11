# 🛡️ Fraud Detection Intelligence Platform

An AI-powered Fraud Detection Intelligence Platform built using FastAPI, Streamlit, PostgreSQL, Docker, and Machine Learning.

The platform detects potentially fraudulent financial transactions using a trained Random Forest model and provides interactive analytics dashboards, JWT authentication, prediction history tracking, and fraud probability scoring.

The application supports both real-time and batch fraud detection while maintaining secure user authentication and prediction history management.

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

## Installation

### Clone Repository

```bash
git clone https://github.com/kashishcrafts/Fraud-Detection-Intelligence-Platform.git
cd Fraud-Detection-Intelligence-Platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
## Docker Setup

### Build Containers

```bash
docker compose up --build -d
```

### View Running Containers

```bash
docker ps
```

### Stop Containers

```bash
docker compose down
```

### Access Services

FastAPI

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

Streamlit Dashboard:

```text
http://localhost:8501

```
## API Endpoints
GET     /
GET     /health

POST    /register
POST    /login

POST    /predict
POST    /predict-batch

GET     /predictions

## Screenshots

### Login Page
![Login](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Prediction History
![History](screenshots/history.png)

### ROC Curve
![ROC](screenshots/roc.png)

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

