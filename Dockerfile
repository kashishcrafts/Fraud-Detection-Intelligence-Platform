<<<<<<< HEAD
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501

=======
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501

>>>>>>> d7cc06efc5da1142cb42abd2819e93cfde5d83bb
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]