import os
import time
import sched
import requests
from datetime import datetime

loop = sched.scheduler(time.time, time.sleep)


def my_loop(scheduler_loop):
    scans = requests.get("http://127.0.0.1:8080/api/scans/").json()
    for scan in scans:
        response = os.system(f"curl -s {scan['domain']} -o NUL")
        if response == 0:
            scan['status'] = "Complete"
        else:
            scan['status'] = "Error"
        print(f"{scan['scan_id']} - {datetime.now()} - domain: {scan['domain']} -> {scan['status']}")
        requests.put("http://127.0.0.1:8080/db-api/", data=scan)
    loop.enter(10, 1, my_loop, (scheduler_loop,))


loop.enter(5, 1, my_loop, (loop,))
loop.run()
