FROM python:3.9.5-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV POETRY_VIRTUALENVS_CREATE false
ENV DJANGO_SETTINGS_MODULE=school_portal.settings.dev

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"
COPY poetry.lock .
COPY pyproject.toml .

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --only main --no-interaction --no-ansi
RUN pip install gunicorn

COPY . .
RUN chmod a+x /app/start_server.sh
ENTRYPOINT ["/app/start_server.sh"]
