from threading import *
from time import sleep

def even():         
    for z in range(1,51):
        sleep(0.2)
        print(z*2,end=' ')

def odd():          
    for z in range(1,51):
        sleep(0.2)
        print(z*2-1)

e1=Thread(target=even)
o1=Thread(target=odd)
e1.start()
o1.start()

# e1.join()
# o1.join()
