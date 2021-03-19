import uuid
import requests
from flask import request
from flask_restful import Resource


class Ingest(Resource):
    """
    Ingest - client api to create new domain scans
    post: add a new scan for a domain and get a unique id for the scan
    """

    def post(self):
        data = request.form
        domain = data['domain']
        scan_id = str(uuid.uuid4())
        db_post_status = requests.post('http://127.0.0.1:8080/db-api/scan/',
                                       data={"scan_id": scan_id, "domain": domain}).json()
        if db_post_status['result'] == "success":
            return {"scan_id": scan_id}
        else:
            return {"result": "Something went wrong, please try again"}
