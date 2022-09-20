from threading import *
from time import sleep

class Even(Thread):
    def even(self):          #Instance method
        for z in range(1,51):
            print(z*2,end=' ')
            sleep(5)

class Odd(Thread):
    def odd(self):          #Instance method
        for z in range(1,51):
            print(z*2-1)
            sleep(5)

e1=Even()
o1=Odd()
e1.even()
o1.odd()