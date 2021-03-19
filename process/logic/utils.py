import os
from datetime import datetime
import requests
from process.logic.conf import Conf


def get_new_requests():
    return requests.get(f"{Conf.BASE_API_URL}{Conf.GET_NEW_REQ_URL}").json()


def process_scan(scan):
    response = os.system(f"curl -s {scan['domain']} -o NUL")
    scan['status'] = Conf.COMPLETE_STATUS if response == 0 else Conf.ERROR_STATUS
    print(f"{scan['scan_id']} - {datetime.now()} - domain: {scan['domain']} -> {scan['status']}")
    requests.put(f"{Conf.BASE_API_URL}{Conf.UPDATE_SCAN_STATUS_URL}", data=scan)


def process_scans_bulk(scans):
    for scan in scans:
        process_scan(scan)
