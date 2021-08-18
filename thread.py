import threading
import thread2
import time
import os
import thread3
class HP(threading.Thread):
    def __init__(self,myhp,enemyhp,attack1,depense,hddm,wtdm,firedm):
        self.st1=thread2.Enemy()
        self.st1.start()
        self.myhp=myhp
        self.enemyhp=enemyhp
        self.myhealth=myhp
        self.enemyhealth=enemyhp
        self.attack1=attack1
        self.attack2=1
        self.depense=depense
        self.hddm=hddm
        self.wtdm=wtdm
        self.firedm=firedm
        self.mp=Mana(0,100)
        self.mp.start()
        
        threading.Thread.__init__(self)
    def run(self):
        self.baseattack()
   
        
    def printhp(self):
            if self.enemyhealth/self.enemyhp>=0.95:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.9 and self.enemyhealth/self.enemyhp<0.95:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.85 and self.enemyhealth/self.enemyhp<0.9:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.8 and self.enemyhealth/self.enemyhp<0.85:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.75 and self.enemyhealth/self.enemyhp<0.8:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.7 and self.enemyhealth/self.enemyhp<0.75:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.65 and self.enemyhealth/self.enemyhp<0.7:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.6 and self.enemyhealth/self.enemyhp<0.65:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.55 and self.enemyhealth/self.enemyhp<0.6:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.5 and self.enemyhealth/self.enemyhp<0.55:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.45 and self.enemyhealth/self.enemyhp<0.5:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □  '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.4 and self.enemyhealth/self.enemyhp<0.45:
                print('hp   ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.35 and self.enemyhealth/self.enemyhp<0.4:
                print('hp   ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.3 and self.enemyhealth/self.enemyhp<0.35:
                print('hp   ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.25 and self.enemyhealth/self.enemyhp<0.3:
                print('hp   ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □  '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.2 and self.enemyhealth/self.enemyhp<0.25:
                print('hp   ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.15 and self.enemyhealth/self.enemyhp<0.2:
                print('hp   ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp>=0.1 and self.enemyhealth/self.enemyhp<0.15:
                print('hp   ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.enemyhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
            elif self.enemyhealth/self.enemyhp<=0:
                print('hp'+str(self.myhealth)+'/'+str(self.enemyhp)+' 당신이 적에게 '+str(self.attack1)+'의 데미지로 공격했습니다.')
                os.exit

    def printmyhp(self):
            if self.myhealth/self.myhp>=0.95:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.9 and self.myhealth/self.myhp<0.95:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.85 and self.myhealth/self.myhp<0.9:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.8 and self.myhealth/self.myhp<0.85:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.75 and self.myhealth/self.myhp<0.8:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.7 and self.myhealth/self.myhp<0.75:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.65 and self.myhealth/self.myhp<0.7:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.6 and self.myhealth/self.myhp<0.65:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □  '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.55 and self.myhealth/self.myhp<0.6:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.5 and self.myhealth/self.myhp<0.55:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.45 and self.myhealth/self.myhp<0.5:
                print('hp   ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.4 and self.myhealth/self.myhp<0.45:
                print('hp   ■ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.35 and self.myhealth/self.myhp<0.4:
                print('hp   ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.3 and self.myhealth/self.myhp<0.35:
                print('hp   ■ ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.25 and self.myhealth/self.myhp<0.3:
                print('hp   ■ ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.2 and self.myhealth/self.myhp<0.25:
                print('hp   ■ ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.')
            elif self.myhealth/self.myhp>=0.15 and self.myhealth/self.myhp<0.2:
                print('hp   ■ ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다. 체력이 매우 없습니다. 포션을 구입하세요!')
            elif self.myhealth/self.myhp>=0.1 and self.myhealth/self.myhp<0.15:
                print('hp   ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ '+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다. 체력이 매우 없습니다. 포션을 구입하세요!')
            elif self.myhealth/self.myhp<=0:
                print('hp   ■ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □'+str(self.myhealth)+'/'+str(self.myhp)+' 적이 당신에게 '+str(self.st1.a)+'의 데미지로 공격했습니다.  체력이 매우 없습니다. 포션을 구입하세요!')
                os.exit
            
    def baseattack(self):
        while True:
            self.enemyhealth=self.enemyhealth-self.attack1
            
            self.myhealth=self.myhealth-self.st1.a
            time.sleep(1)
            if self.depense==1:
                self.st1.a-=3
            if self.myhealth<=0:
                break

    def headbutt(self):
        if self.mp.mana>=40:
            self.mp.mana-=40
            self.hddm=40
            self.enemyhealth-=self.hddm

        
    def watergun(self):
        if self.mp.mana>=60:
            self.mp.mana-=60
            self.wtdm=60
            self.enemyhealth-=self.wtdm
        
    def fire(self):
        if self.mp.mana>=100:
            self.mp.mana-=100
            self.firedm=200
            self.enemyhealth-=self.firedm 

    def manaupdate(self):
        print('MP : '+str(self.mp.mana)+'/'+str(self.mp.maxmana))    
        

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
            
            




        
   
    

