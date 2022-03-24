import json
from flask import Response, request
from ..model.model import *
from cryptography.fernet import Fernet
from ..config.db import db


def create_routes(app):
    @app.route("/")
    def home():
        return "hello"

    @app.route("/register", methods=["POST"])
    def register_user():
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        username = request.json.get("username", None)

        try:
            user = User(
                email=email,
                password=encrypt_pass(password),
                username=username
            )
            db.session.add(user)
            db.session.commit()
            return get_response(201, "register user", user.to_json(), "User registered")
        except Exception as e:
            print(e)
            return get_response(404, "shit", e)


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
