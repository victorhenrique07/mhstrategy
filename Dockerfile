FROM python:3.10 AS builder

ADD . /code

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URI=mariadb+psycopg2://root:94082@localhost/MHStrategy

RUN poetry install

EXPOSE 3000

CMD [ "flask", "run" ]