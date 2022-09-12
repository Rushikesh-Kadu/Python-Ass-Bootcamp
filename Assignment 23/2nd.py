def odd(n):
    x=1
    while n:
        yield x*2-1
        x+=1
        n-=1

for x in odd(10):
    print(x)