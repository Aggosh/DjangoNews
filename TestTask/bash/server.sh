#!/bin/bash

python ./manage.py migrate
gunicorn TestTask.wsgi:application --bind 0000:8888 --daemon
