def odd(N):
    if(N>0):
        print(N*2-1)
        odd(N-1)
odd(10)