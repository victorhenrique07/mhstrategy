from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import getenv

DATABASE_URI = getenv("DATABASE_URI")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from flask_app.controller import auth
    from flask_app.model import User, db

    app.register_blueprint(auth, url_prefix='/')
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app, db)

    db.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()
    return app



