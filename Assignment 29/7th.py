from keyword import *
def countKeyword(fileName):
    f=open(fileName,'r')
    count=0
    for y in f.readlines():
        y=y.strip()
        for x in kwlist:
            if ' ' not in y:
                if x+':'==y:
                    print(x)
                    count+=1
            else:
                if x in y.split(' '):
                    print(x,'  ')
                    count+=1
    print("Total keyword in {} is {}".format(f.name,count))

countKeyword('Assignment 29/6th.py')