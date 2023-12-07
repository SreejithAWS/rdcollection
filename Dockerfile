# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt openpyxl Flask-SQLAlchemy
 
EXPOSE 5000

CMD ["python", "app.py"]