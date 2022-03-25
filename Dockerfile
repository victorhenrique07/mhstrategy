FROM python:3.10 AS builder

WORKDIR /app

COPY . /app/

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URI="mariadb+pymysql://rick:12345@localhost/MHStrategy"

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

EXPOSE 3000

CMD [ "poetry", "run", "flask", "run" ]