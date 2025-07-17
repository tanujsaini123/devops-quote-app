FROM python:3.10-slim

WORKDIR /app

COPY backend/app.py .
RUN pip install flask

COPY frontend ./frontend

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
