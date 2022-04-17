from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Monster(db.Model):
    __tablename__ = 'monsters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), unique=False, nullable=False)
    weakness = db.Column(db.String(255), unique=False, nullable=False)
    strong = db.Column(db.String(255), unique=False, nullable=False)
    build = db.Column(db.Text, unique=False, nullable=False)

    @classmethod
    def build_new_monster(cls, name, weakness, strong, build):
        return Monster(name, weakness, strong, build)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    @classmethod
    def build_new_user(cls, username, email, password):
        return User(username=username, email=email, password=password)
    
