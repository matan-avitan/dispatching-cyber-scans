import time
import sched

loop = sched.scheduler(time.time, time.sleep)


def my_loop(scheduler_loop):
    print("Hello")
    loop.enter(5, 1, my_loop, (scheduler_loop,))


loop.enter(5, 1, my_loop, (loop,))
loop.run()
