FROM python:3.10-slim

WORKDIR /app

COPY backend/app.py .

RUN pip install flask

CMD ["python", "app.py"]
