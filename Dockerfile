FROM python:3.10 AS builder

ADD . /code

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install Flask && pip install cryptography && pip install flask-sqlalchemy

EXPOSE 3000

CMD [ "flask", "run" ]