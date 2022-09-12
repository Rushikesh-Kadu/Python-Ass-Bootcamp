def prime(n):
    x=2
    while n:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            yield x
            n-=1
        x+=1
for x in prime(10):
    print(x,end=' ')