import uuid
import requests
from ingest.app.conf import Conf
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('domain', type=str, help="domain for scan")


class Ingest(Resource):
    """
    Ingest - client api to create new domain scans
    post: add a new scan for a domain and get a unique id for the scan
    """

    def post(self):
        args = parser.parse_args()
        domain = args['domain']
        scan_id = str(uuid.uuid4())
        db_post_status = requests.post(f'{Conf.BASE_API_URL}{Conf.POST_NEW_SCAN_URL}',
                                       data={"scan_id": scan_id, "domain": domain}).json()
        if db_post_status['result'] == Conf.API_STATUS:
            return {"scan_id": scan_id}
        else:
            return {"result": "Something went wrong, please try again"}
