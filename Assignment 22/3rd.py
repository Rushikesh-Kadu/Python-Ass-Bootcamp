def sumEven(N):
    if N==1:
        return 2
    return N*2+sumEven(N-1)

print(sumEven(4))