"""Short summary: scheduling means running a task automatically at a set time,
after a delay, or on a repeating interval, instead of running it immediately.
Python's standard library provides the 'sched' module for this."""


# (Linux learn)
# cron, Airflow, even while loop you can use schedulling

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def say_hello():
    print("Hello, scheduled task executed!")

scheduler.enter(2, 1, say_hello)  # run say_hello() after a 2 second delay
scheduler.run()


# cron
# crontab -e
# cron formula (crontab guru)


# below run cron add scheduling  => system off but this code is running while

#nohup python3 while_true_scheduling.py >> data.log &
# ps-aux   cmd
# show running list task
# kill -9 1222