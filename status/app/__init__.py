from flask import Flask
from flask_restful import Api
from status.app.resources.status import Status


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Status, "/status/<string:scan_id>/")
    return app
