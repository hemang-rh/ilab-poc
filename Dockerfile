FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

RUN mkdir logs && chmod 777 logs

COPY pyproject.toml poetry.lock* ./
COPY ilab_poc/ ./ilab_poc/
COPY entrypoint.sh /

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
