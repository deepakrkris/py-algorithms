# Implement a job scheduler which takes in a function f and an integer n,
# and calls f after n milliseconds
#
#

import threading
from time import sleep
from datetime import datetime

class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        print(n)
        def sleep_then_call():
            sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()

s = Scheduler()
print(datetime.now())
s.delay( lambda : print(datetime.now()) , 10000)
