import imp
from re import S


from threading import Thread
s=0
def add50():
    for x in range(1,51):
        global s
        s+=x

def add100():
    for x in range(51,101):
        global s
        s+=x
    
add1=Thread(target=add50)
add2=Thread(target=add100)

add1.start()
add2.start()
print(s)