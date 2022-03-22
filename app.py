from flask_app.controller.controller import create_routes
from flask import Flask

app = Flask(__name__)
create_routes(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
