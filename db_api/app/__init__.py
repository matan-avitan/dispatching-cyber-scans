from flask import Flask
from flask_restful import Api
from db_api.app.models.scan_model import db
from db_api.app.resources.scan_api import ScanApi
from db_api.app.resources.scans_list_api import ScansListApi


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    api.add_resource(ScanApi, "/db-api/", '/db-api/<string:scan_id>/')
    api.add_resource(ScansListApi, "/api/scans/")
    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
