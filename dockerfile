# base image
FROM python:3.10.2-alpine

# where your code lives
WORKDIR .

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DJANGO_SECRET_KEY
ARG SENTRY_DSN
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV SENTRY_DSN=$SENTRY_DSN

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

# port where the Django app runs  
EXPOSE 8000

RUN python3 manage.py collectstatic --noinput

# start server
CMD python3 manage.py runserver 0.0.0.0:8000