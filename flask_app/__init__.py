from flask import Flask
from db import db
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+pymysql://root:12345@localhost/MHStrategy"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .controller.controller import auth
    
    app.register_blueprint(auth, url_prefix='/')
    
    return app
