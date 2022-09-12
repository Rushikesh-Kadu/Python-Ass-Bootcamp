def nat(n):
    x=1
    while n:
        yield x
        x+=1
        n-=1