import time
import sched
from process.conf import Conf
from process.utils import get_new_requests, process_scans_bulk

loop = sched.scheduler(time.time, time.sleep)


def process(scheduler_loop):
    """
    process component try to get every 10 seconds all the new scans.
    it scans each one and update the status.
    process use in curl command to check if the domain is alive.
    """
    try:
        scans = get_new_requests()
        process_scans_bulk(scans)
    except Exception as e:
        print(str(e))
    finally:
        loop.enter(Conf.LOOP_INTERVAL, Conf.LOOP_PRIORITY, process, (scheduler_loop,))


loop.enter(Conf.LOOP_INTERVAL, Conf.LOOP_PRIORITY, process, (loop,))
loop.run()
