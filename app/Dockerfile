FROM python:3.6
ARG DJANGO_ENV

ADD requirements /app/requirements
WORKDIR /app/

RUN pip install -r requirements/$DJANGO_ENV.txt

RUN adduser --disabled-password --gecos '' app