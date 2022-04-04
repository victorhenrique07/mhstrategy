import json
from flask import Response, redirect, request, Blueprint, render_template, url_for
from ..model.model import *
from cryptography.fernet import Fernet
from ..db import db

auth = Blueprint('auth', __name__)


@auth.route("/")
def home():
    return "hi"

@auth.route("/register", methods=['GET', 'POST'])
def register_user():
    #find_email = User.query.filter_by(email=email).first()
    try:
        if request.method == 'POST':
            email = request.form["email"]
            username = request.form["username"]
            password = request.form["password"]
            user = User(email,encrypt_pass(password),username)

            db.session.add(user)
            db.session.commit()

        return render_template("register.html")
    except Exception as e:
        print(e)
        return "deu ruim"


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(
        json.dumps(body),
        status=status,
        mimetype="authlication/json"
    )


def encrypt_pass(password):
    password = bytes(password, encoding='utf8')
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password)
    return token
