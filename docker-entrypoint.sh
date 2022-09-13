#!/bin/sh
set -e

echo Run django migrations
python manage.py migrate --noinput || exit 0

echo Creating superuser
# python manage.py createsuperuser --no-input

# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(email='admin@gmail.com', password='admin',username='admins')" | python manage.py shell

echo Collect staticfiles
python manage.py collectstatic --noinput --clear

set -xe

echo Running server
gunicorn --bind 0.0.0.0:8000 config.wsgi:application --workers 2