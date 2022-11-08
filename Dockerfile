# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9.5-slim-buster

# Add user that will be used in the container.
# RUN useradd wagtail
WORKDIR /app

# Port used by this container to serve HTTP.

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.

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
# ENV DJANGO_SETTINGS_MODULE=config.settings.dev
ENV DJANGO_SETTINGS_MODULE=school_portal.settings.dev

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install the project requirements.
RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"
COPY poetry.lock .
COPY pyproject.toml .

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --only main --no-interaction --no-ansi
RUN pip install gunicorn

# Use /app folder as a directory where the source code is stored.
COPY . .
RUN chmod a+x /app/start_server.sh
ENTRYPOINT ["/app/start_server.sh"]

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
# RUN chown wagtail:wagtail /app

# # Copy the source code of the project into the container.
# COPY --chown=wagtail:wagtail . .

# # Use user "wagtail" to run the build commands below and the server itself.
# USER wagtail

# Collect static files.
# RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
# CMD set -xe; python manage.py migrate --noinput; gunicorn school_portal.wsgi:application
