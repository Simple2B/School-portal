set -e

echo version
python manage.py --version
pwd
ls -a
echo started migration
python manage.py migrate
echo collect static
python manage.py collectstatic --noinput --clear
echo runserver
set -xe

echo Running server
gunicorn --bind 0.0.0.0:8000 school_portal.wsgi:application --workers 2
