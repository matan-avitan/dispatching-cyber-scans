import uuid
import requests
from flask_restful import Resource
from json import loads
from flask import request


class Ingest(Resource):

    def post(self):
        data = loads(request.data)
        domain = data['domain']
        scan_id = str(uuid.uuid4())
        db_post_status = requests.post('http://127.0.0.1:8080/db-api/',
                                       data={"scan_id": scan_id, "domain": domain}).json()
        if db_post_status['result'] == "success":
            return {"scan-id": scan_id}
        else:
            return {"result": "sorry, something got wrong try again"}