from flask_restful import Resource
from flask import request
from json import loads
from db_api.app.models.scan_model import db, ScanModel
from datetime import datetime


class DBApi(Resource):

    def post(self):
        data = loads(request.data)
        scan = ScanModel(scan_id=data['scan_id'], domain=data['domain'], insertion_time=datetime.now(),
                         status="Accepted")
        db.session.add(scan)
        db.session.commit()
        return {}


