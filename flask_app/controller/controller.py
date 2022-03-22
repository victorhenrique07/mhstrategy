import json
from flask import Response, request
from flask_app.config.db import db
from flask_app.model.model import *
from cryptography.fernet import Fernet


def create_routes(app):
    @app.route("/")
    def home():
        return "hello"

    @app.route("/register", methods=["POST"])
    def register_user():
        body = request.get_json()

        try:
            user = User(
                email=body["email"],
                password=body["password"],
                username=body["username"]
            )
            user.password = encrypt_pass(user.password)
            return user.password
        except Exception as e:
            print(e)
            return "shit"


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(
        json.dumps(body),
        status=status,
        mimetype="application/json"
    )


def encrypt_pass(password):
    password = bytes(password, encoding='utf8')
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password)
    return token

