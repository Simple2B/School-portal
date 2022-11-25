# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.9.5

WORKDIR /app

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

# Use /app folder as a directory where the source code is stored.
COPY . .
RUN chmod a+x /app/start_server.sh
ENTRYPOINT ["/app/start_server.sh"]
