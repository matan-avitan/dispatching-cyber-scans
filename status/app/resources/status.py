import requests
from status.app.conf import Conf
from flask_restful import Resource


class Status(Resource):
    """
    Status component is client api to know what is the status of a scan.
    get - send a scan id and get the status of the scan.
    """

    def get(self, scan_id):
        scan_status = requests.get(f'{Conf.BASE_API_URL}{Conf.GET_STATUS_URL}{scan_id}/').json()
        return {"result": scan_status}
