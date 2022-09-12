def odd(N):
    if N>0:
        odd(N-1)
        print(N*2-1)

odd(10)