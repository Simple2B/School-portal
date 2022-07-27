#!/bin/sh
set -e
echo Run django migrations
python manage.py migrate --noinput || exit 0
echo Collect staticfiles
(python manage.py collectstatic --noinput --clear &&
touch staticfiles/.gitignore && echo '# Ignore everything in this directory'\\n'*'\\n'# Except this file'\\n'!.gitignore' >> staticfiles/.gitignore; exit 0)

exec "$@"
