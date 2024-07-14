#!/bin/bash

python manage.py migrate

pytest

gunicorn --config gunicorn_config.py culinary_api.wsgi:application

