FROM python:3.12

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN  pip install -r requirements.txt --no-cache-dir

COPY . .

ENV SECRET_KEY="django-insecure-k2&&&d6zqu#6x*qgz28$&r1)00+$&#a8ne5_d_)5i4lcalbk=w"
ENV CELERY_BROKER_URL="redis://redis:6379/0"
ENV CELERY_RESULT_BACKEND="redis://redis:6379/0"

RUN mkdir -p /app/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
