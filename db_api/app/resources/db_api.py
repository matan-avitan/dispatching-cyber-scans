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

    def get(self, scan_id):
        scan_status = ScanModel.query.filter_by(scan_id=scan_id).first()
        return {"status": scan_status.status, "scan_id": scan_id}
