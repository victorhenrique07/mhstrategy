from flask_app.config.db import db


class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    weakness = db.Column(db.String(255), unique=False, nullable=False)
    strong = db.Column(db.String(255), unique=False, nullable=False)
    build = db.Column(db.Text, unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "weakness": self.weakness,
            "strong": self.strong,
            "build": self.build,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(230), unique=False, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "username": self.username
        }