from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from cryptography.fernet import Fernet

db = SQLAlchemy()

def encrypt_pass(password):
    password = bytes(password, encoding='utf8')
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(password)
    return token

class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    weakness = db.Column(db.String(255), unique=False, nullable=False)
    strong = db.Column(db.String(255), unique=False, nullable=False)
    build = db.Column(db.Text, unique=False, nullable=False)

    @classmethod
    def build_new_monster(cls, name, weakness, strong, build):
        return Monster(name, weakness, strong, build)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(230), unique=False, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)

    @classmethod
    def build_new_user(cls, username, email, password):
        return User(username=username, email=email, password=encrypt_pass(password))
