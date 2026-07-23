import time
from datetime import datetime

def task():
    # This is the code thet runs every 2 minites
    with open("time_log.txt", "a") as f:
        f.write(f"Script run at:{datetime.now()}\n")
    print(f"Task run at:{datetime.now()}")

#run forever
while True:
    task()
    time.sleep(120) # 2 min after added