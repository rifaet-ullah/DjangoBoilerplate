#!/bin/bash

python3 manage.py collectstatic --no-input
python3 manage.py migrate
gunicorn -w 1 -b :5000 app.wsgi:application
