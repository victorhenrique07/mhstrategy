import json
from flask import Response, request
from flask_app.config.db import db
from flask_app.model.model import *
import bcrypt


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
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User(
                email=email,
                password=hashed,
                username=username
            )
            db.session.add(user)
            db.session.commit()
            return f'Welcome! {email}', 201
          #  return get_response(201, "register user", user.to_json(), "User registered")
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
