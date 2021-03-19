import requests
from flask_restful import Resource
from json import loads
from flask import request


class Status(Resource):

    def get(self, scan_id):
        scan_status = requests.get(f'http://127.0.0.1:8080/db-api/scan/{scan_id}/').json()
        return {"result": scan_status}
