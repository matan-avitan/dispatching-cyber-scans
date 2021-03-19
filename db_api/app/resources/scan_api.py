from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta

from db_api.app.models.scan_model import db, ScanModel

parser = reqparse.RequestParser()
parser.add_argument('scan_id', type=str, help='unique scan id')
parser.add_argument('domain', type=str, help='domain to scan')
parser.add_argument('status', type=str, help='status of the scan')


class ScanApi(Resource):
    """
    Scan Api - request with one scan.
    post - add new scan to the db with Accepted status
    get - get a status for a scan from specific scan id
    put - update a scan with new status like (Running, Error, Completed)
    """

    def post(self):
        try:
            args = parser.parse_args()
            scan = ScanModel(scan_id=args['scan_id'], domain=args['domain'], insertion_time=datetime.now(),
                             status="Accepted")
            db.session.add(scan)
            db.session.commit()
            return {"result": "success"}
        except Exception as e:
            return {"result": "Failed", "error": str(e)}

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
        try:
            args = parser.parse_args()
            scan = ScanModel.query.filter_by(scan_id=args['scan_id']).filter_by(domain=args['domain']).first()
            scan.status = args['status']
            db.session.commit()
            return {"result": "successfully update status"}
        except Exception as e:
            return {"result": "Failed", "error": str(e)}
