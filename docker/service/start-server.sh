#!/bin/bash

python manage.py migrate

uwsgi --ini /app/docker/service/uwsgi.ini
