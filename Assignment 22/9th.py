def oct(N):
    if N>0:
        print(N%8)
        oct(N//8)