from flask import redirect, request, Blueprint, render_template, url_for
from flask_app.model import *
from flask_app import db
from flask_login import login_required, login_user, logout_user, current_user
import logging

auth = Blueprint('auth', __name__)

@auth.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user.id)


@auth.route("/home/builds")
def monsters_build():
    return render_template("monsters.html")


@auth.route("/register", methods=['GET', 'POST'])
def register_user():
    try:
        if request.method == 'POST':
            email = request.form["email"]
            username = request.form["username"]
            password = request.form["password"]
            user = User.build_new_user(email, password, username)
            search_email = User.query.filter_by(email=email).first()

            if search_email:
                return redirect(url_for("auth.login"))

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))

        return render_template("register.html")
    except Exception as e:
        print(e)
        return "deu ruim"

@auth.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == 'POST':
            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(email=email).first()

            if not user:
                logging.error("E-mail or password incorrect. Try again.")
                return redirect(url_for("auth.login"))

            login_user(user)
            logging.info("User Logged!")
            return redirect(url_for("auth.home"))
        return render_template("login.html")
    except Exception as e:
        print(e)
    return 400, "Error"
