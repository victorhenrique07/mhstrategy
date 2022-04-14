FROM python:3.10 AS builder

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URI=mariadb+psycopg2://root:94082@localhost/MHStrategy

RUN pip install flask

EXPOSE 3000

CMD [ "poetry", "run", "flask", "run" ]