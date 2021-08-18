import threading
import time
import thread
class Mana(threading.Thread):
    def __init__(self,mana,maxmana):
        threading.Thread.__init__(self)
        self.mana=mana
        self.maxmana=maxmana
        
    def run(self):
        while True:
            self.mana+=1
            time.sleep(0.1)
            if self.mana >= self.maxmana:
                self.mana=self.maxmana
                break
            

class UpdateMana:
    def __init__(self):
        pass
        self.asdf=Mana(0,100)
        self.asdf.start()
        
    def manaupdate(self):
        print('MP : '+str(self.asdf.mana)+'/'+str(self.asdf.maxmana))
    