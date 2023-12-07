# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt \
 && pip install openpyxl

EXPOSE 5000

CMD ["python", "app.py"]