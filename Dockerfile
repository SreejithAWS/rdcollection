# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y \
    libx11-6 \
    libxcb1 \
    libxtst6 \
    libxrender1 \
    libxi6 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

CMD ["python", "app.py"]