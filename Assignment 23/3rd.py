def even(n):
    x=1
    while n:
        yield x*2
        x+=1
        n-=1