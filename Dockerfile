FROM python:3.8

RUN mkdir /app
WORKDIR /app

ADD TestTask /app/
ADD Pipfile Pipfile.lock /app/

ENV PYTHONDONTWRITBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install --upgrade pip &&\
    pip3 install pipenv &&\
    pipenv install --system --dev

RUN apt-get update && apt-get -y install cron

EXPOSE 8888
CMD gunicorn TestTask.wsgi:application --bind 0000:$PORT
