FROM python:3.10 AS builder

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 3000

CMD [ "poetry", "run", "flask", "run" ]