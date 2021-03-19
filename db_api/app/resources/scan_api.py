from flask import request
from flask_restful import Resource
from datetime import datetime, timedelta

from db_api.app.models.scan_model import db, ScanModel


class ScanApi(Resource):
    """
    Scan Api - request with one scan.
    post - add new scan to the db with Accepted status
    get - get a status for a scan from specific scan id
    put - update a scan with new status like (Running, Error, Completed)
    """

    def post(self):
        try:
            data = request.form
            scan = ScanModel(scan_id=data['scan_id'], domain=data['domain'], insertion_time=datetime.now(),
                             status="Accepted")
            db.session.add(scan)
            db.session.commit()
            return {"result": "success"}
        except Exception:
            return {"result": "Failed"}

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
        scan = ScanModel.query.filter_by(scan_id=data['scan_id']).filter_by(domain=data['domain']).first()
        scan.status = data['status']
        db.session.commit()
        return {"result": "successfully update status"}
