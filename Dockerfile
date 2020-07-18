FROM python:3.8

ENV PYTHONDONTWRITBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get -y install cron

CMD gunicorn TestTask.wsgi:application --bind 0.0.0.0:$PORT
