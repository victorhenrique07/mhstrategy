FROM python:3.10 AS builder

ADD . /code

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=1.1.1.1
ENV DATABASE_URI=mariadb+psycopg2://root:94082@localhost/MHStrategy

RUN pip install flask && pip install cryptography \
    && pip install flask-sqlalchemy && pip install python-dotenv \
    && pip install psycopg2

EXPOSE 3000

CMD [ "flask", "run" ]