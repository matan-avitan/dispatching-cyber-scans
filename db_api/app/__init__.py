from flask import Flask
from flask_restful import Api
from db_api.app.models.scan_model import db
from db_api.app.resources.scan_api import ScanApi
from db_api.app.resources.scans_list_api import ScansListApi


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # config and init the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # routes
    api.add_resource(ScanApi, "/db-api/scan/", '/db-api/scan/<string:scan_id>/')
    api.add_resource(ScansListApi, "/db-api/scans/")

    # drop old table and create new from modals
    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
