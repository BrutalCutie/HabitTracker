FROM python:3.12.3

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

#COPY requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir


ENV CELERY_BROKER_URL="redis://redis:6379/0"
ENV CELERY_RESULT_BACKEND="redis://redis:6379/0"


