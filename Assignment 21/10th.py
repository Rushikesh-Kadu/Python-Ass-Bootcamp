def revNum(N):
    if N>0:
        print(N%10,end='')
        revNum(N//10)

revNum(1234)