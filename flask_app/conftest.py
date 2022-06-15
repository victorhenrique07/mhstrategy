from pytest import fixture
from app import app
from flask_app import create_app

@fixture
def client():
    client = app.test_client()
    yield client
    
@fixture
def flask_app():
    flask_app = create_app()
    return flask_app