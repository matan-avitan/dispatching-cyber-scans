from flask_restful import Resource
from flask import request
from json import loads
from db_api.app.models.scan_model import db, ScanModel
from datetime import datetime, timedelta


class ScanApi(Resource):

    def post(self):
        data = loads(request.data)
        scan = ScanModel(scan_id=data['scan_id'], domain=data['domain'], insertion_time=datetime.now(),
                         status="Accepted")
        db.session.add(scan)
        db.session.commit()
        return {"result": "successfully got new scan"}

    def get(self, scan_id):
        last_twenty_minutes = datetime.now() - timedelta(minutes=20)
        scan_status = ScanModel.query.filter(ScanModel.insertion_time > last_twenty_minutes).filter_by(
            scan_id=scan_id).first()
        if scan_status is None:
            status = "NOT FOUND"
        else:
            status = scan_status.status
        return {"status": status, "scan_id": scan_id}

    def put(self):
        data = request.form
        scan = ScanModel.query.filter(scan_id=data['scan_id']).filter(domain=data['domain']).first()
        scan.status = data['status']
        db.session.commit()
        return {"result": "successfully update status"}
