import json
from flask import Response, request


def create_routes(app):
    @app.route("/")
    def home():
        return "hello"


def get_response(status, resource_name, resource, message=False):
    body = {resource_name: resource}
    if message:
        body["message"] = message

    return Response(
        json.dumps(body),
        status=status,
        mimetype="application/json"
    )
