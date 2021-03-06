from flask_restful import Resource
from flask_restful import marshal_with
from db_api.app.models.scan_model import db, ScanModel
from db_api.app.resources.resource_utils import error_handler
from db_api.app.serializers.scan_serializer import resource_fields


class ScansListApi(Resource):
    """
    Scan List Api - for bulk of new scans
    get - return all new scans and update their status to Running
    """

    @error_handler
    @marshal_with(resource_fields)
    def get(self):
        scans = ScanModel.query.filter_by(status="Accepted").all()
        for scan in scans:
            scan.status = 'Running'
        db.session.commit()
        return scans
