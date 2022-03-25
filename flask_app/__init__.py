from flask import Flask
from os import getenv
from .controller.controller import auth
from flask_migrate import Migrate
from .db import db

DATABASE_URI = getenv("DATABASE_URI")

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(auth, url_prefix='/')
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        db.create_all
    return app