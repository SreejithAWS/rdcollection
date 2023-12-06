# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    libx11-6 \
    libxcb1 \
    libxtst6 \
    libxrender1 \
    libxi6 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

EXPOSE 8040

CMD ["python", "app.py"]