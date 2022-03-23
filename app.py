from flask_app.controller.controller import create_routes
from flask import Flask
from flask_migrate import Migrate
import os
from flask_app.config.db import db

DATABASE_URI = os.getenv('DATABASE_URI')

app = Flask(__name__)
create_routes(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')