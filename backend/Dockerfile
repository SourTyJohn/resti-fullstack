FROM python:3.11-slim AS builder

# - POETRY -
ENV POETRY_VERSION=2.1.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"
# --


WORKDIR /backend

COPY poetry.lock pyproject.toml ./
RUN python3 -m venv .venv \
    && poetry install --no-root --no-ansi --without=dev
ENV PATH="./.venv/bin:$PATH"

# ---------------------------------------------------------------------

FROM python:3.11-slim AS runner
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/backend/.venv/bin:$PATH"

# ---------------------------------------------------------------------

WORKDIR /backend
COPY --from=builder /backend/.venv ./.venv
COPY ./app ./app
# 
COPY ./alembic.ini ./alembic.ini
COPY ./migration ./migration
#
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
COPY ./manage.py ./manage.py
ENTRYPOINT [ "entrypoint.sh" ]
