FROM python:3.9-slim AS app

ENV PATH=/root/.poetry/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY vendor/get-poetry.py .

RUN python get-poetry.py && rm get-poetry.py
COPY ./pyproject.toml ./poetry.lock ./app ./

RUN poetry config virtualenvs.create false \
 && poetry install --no-dev --no-root --no-interaction --no-ansi

CMD gunicorn --worker-class gevent --workers 3 --bind 0.0.0.0:${APP_PORT} app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
