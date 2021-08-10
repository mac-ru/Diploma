# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY docker/requirements.txt /code/
RUN pip install -r requirements.txt
COPY src/ /code/
ENTRYPOINT python manage.py runserver 0.0.0.0:3000
