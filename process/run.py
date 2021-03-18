import os
import time
import sched
import requests
import datetime

loop = sched.scheduler(time.time, time.sleep)


def my_loop(scheduler_loop):
    print(f"start loop {datetime.datetime.now()}")
    scans = requests.get("http://127.0.0.1:8080/api/scans/").json()
    for scan in scans:
        response = os.system(f"ping -n 1 {scan['domain']}")
        if response == 0:
            status = "Complete"
        else:
            status = "Error"
        requests.put("http://127.0.0.1:8080/db-api/", data={'status': status})
    loop.enter(10, 1, my_loop, (scheduler_loop,))


loop.enter(5, 1, my_loop, (loop,))
loop.run()
