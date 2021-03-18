from flask_restful import Resource

from db_api.app.models.scan_model import db, ScanModel

from flask_restful import marshal_with, fields

resource_fields = {
    'scan_id': fields.String,
    'domain': fields.String,
    'status': fields.String,
}


class ScansListApi(Resource):

    @marshal_with(resource_fields)
    def get(self):
        scans = ScanModel.query.filter_by(status="Accepted").all()
        for scan in scans:
            scan.status = 'Running'
        db.session.commit()
        return scans
