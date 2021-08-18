
import threading

class Game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.choice=None
        
    def run(self):
        while True:
            self.choice=input('선택: ')
            print(self.choice)

        