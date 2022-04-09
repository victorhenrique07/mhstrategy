import json
from flask import Response, redirect, request, Blueprint, render_template, url_for
from ..model.model import *
from cryptography.fernet import Fernet
from ..db import db
from flask_login import login_user, logout_user
import logging

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
            search_email = User.query.filter_by(email=email).first
            search_pass = User.query.filter_by(password=password).first

            if search_email:
                return redirect(url_for("auth.login"))
            elif search_email and not search_pass:
                logging.critical("Wrong password. Try again.")
                return 0

            db.session.add(user)
            db.session.commit()

        return render_template("register.html")
    except Exception as e:
        print(e)
        return "deu ruim"

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            logging.critical("Incorrect e-mail. Try again.")
            return redirect(url_for("auth.login"))
        elif user and not user.verify_password(password):
            logging.critical("Incorrect password. Try again.")
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("auth.home"))


def encrypt_pass(password):
    password = bytes(password, encoding='utf8')
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password)
    return token
