def prime():
    x=2
    while True:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            yield x
        x+=1
it=prime()
while True:
    res=input("\nWants to print Prime number Press Y/N:")
    if res=='y' or res=='Y':
        print(next(it),end=' ')
    elif res=='n' or res=='N':
        break
    else:
        continue