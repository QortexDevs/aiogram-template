FROM python:3.12

WORKDIR /

COPY pyproject.toml poetry.lock* /code/

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install

COPY . /code/
