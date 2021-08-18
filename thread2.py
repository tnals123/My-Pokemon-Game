import threading
import random
import time
class Enemy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            self.a=random.randint(3,10)
            time.sleep(1)