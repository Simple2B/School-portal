# Use an official Python runtime based on Debian 10 as a parent image.
FROM python:3.9

# Add user that will be used in the container.
RUN useradd wagtail

# Set work directory
WORKDIR /usr/src/app

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1
# 2. Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# 3. Install fault handlers for the SIGSEGV, SIGFPE, SIGABRT, SIGBUS, and SIGILL signals
ENV PYTHONFAULTHANDLER 1
# 4. Disable pip's cache files in the container
ENV PIP_NO_CACHE_DIR off
# 5. Don’t periodically check PyPI to determine whether a new version of pip is available for download
ENV PIP_DISABLE_PIP_VERSION_CHECK on
# 6. Keeps Poetry from automatically creates virtual environments
ENV POETRY_VIRTUALENVS_CREATE false
# 7. Add custom environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry self update

# Install the project requirements.
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev --no-interaction --no-ansi

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /usr/src/app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# mark the destination for images as a volume
VOLUME ["/usr/src/app/media/images/"]

# start gunicorn, using a wrapper script to allow us to easily add more commands to container startup:
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
RUN chmod a+x /usr/src/app/docker-entrypoint.sh

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
CMD set -xe; gunicorn --bind 0.0.0.0:8000 config.wsgi:application --workers 2
