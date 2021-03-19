from flask import Flask
from flask_restful import Api
from ingest.resources.ingest import Ingest


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # routes
    api.add_resource(Ingest, "/ingest/")

    return app
