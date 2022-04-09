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

    def __init__(self, name, weakness, strong, build):
        self.name = name
        self.weakness = weakness
        self.strong = strong
        self.build = build



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(230), unique=False, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)

    def __init__(self, email, password, username):
        self.email = email
        self.password = encrypt_pass(password)
        self.username = username
