from flask import Flask
from flask_restful import Api
from db_api.app.models.scan_model import db
from db_api.app.resources.db_api import DBApi


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    api.add_resource(DBApi, "/db-api/", '/db-api/<string:scan_id>/')

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    return app
