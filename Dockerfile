FROM python:3.10 AS builder

ADD . /code

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URI="mariadb+pymysql://rick:12345@localhost/MHStrategy"

RUN pip install flask && pip install cryptography && pip install python-dotenv \
    && pip install pymysql && pip install redis && pip install flask-sqlalchemy
CMD [ "flask", "run" ]