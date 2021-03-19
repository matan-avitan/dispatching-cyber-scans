from flask_restful import fields

resource_fields = {
    'scan_id': fields.String,
    'domain': fields.String,
    'status': fields.String,
}
