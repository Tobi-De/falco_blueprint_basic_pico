#!/bin/sh

python manage.py migrate
falco setup-admin
gunicorn config.wsgi --config="deploy/gunicorn.conf.py"
