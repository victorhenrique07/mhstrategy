from flask import Flask
from .db import db
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://wlmxxjvkbxzalz:466a1ee4eed0338d495cfe18a52a04e54a794e35ff6bc2324e464e0c006efb29@ec2-3-225-213-67.compute-1.amazonaws.com:5432/dfjcq3qk0jsdk3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    from .controller.controller import auth
    
    app.register_blueprint(auth, url_prefix='/')
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app