from flask import Flask
from flask_restful import Api
from ingest.app.resources.ingest import Ingest


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ingest, "/ingest/")
    return app
