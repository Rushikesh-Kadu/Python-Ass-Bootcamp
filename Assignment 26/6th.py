from threading import *
import random
from time import sleep

list=[]
def genList1():
    for x in range(5):
        list.append(random.randint(0,100))
        #sleep(0.2)

def genList2():
    for x in range(5):
        list.append(random.randint(0,100))
        #sleep(0.2)

def genList3():
    for x in range(5):
        list.append(random.randint(0,100))
        #sleep(0.2)

def genList4():
    for x in range(5):
        list.append(random.randint(0,100))
        #sleep(0.2)

def genList5():
    for x in range(5):
        list.append(random.randint(0,100))
       # sleep(0.2)

g1=Thread(target=genList1)
g2=Thread(target=genList2)
g3=Thread(target=genList3)
g4=Thread(target=genList4)
g5=Thread(target=genList5)
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()

print(list)