FROM python:3.11-slim-bullseye

ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
    && apt-get install -y --no-install-recommends $buildDeps \
    && pip install setuptools wheel \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} && \
    cd /usr/local/bin && \
        ln -s /opt/poetry/bin/poetry && \
            poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
COPY src /app/src

WORKDIR /app

RUN poetry install --no-dev


CMD ["poetry", "run", "python", "src/main.py"]
