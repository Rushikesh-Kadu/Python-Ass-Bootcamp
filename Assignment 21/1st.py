def nat(N):
    if N>0:
        nat(N-1)
        print(N)

nat(10)