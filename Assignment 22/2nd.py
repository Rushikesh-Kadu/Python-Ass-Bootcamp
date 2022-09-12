def sumOdd(N):
    if N==1:
        return 1
    return N*2-1+sumOdd(N-1)

print(sumOdd(4))