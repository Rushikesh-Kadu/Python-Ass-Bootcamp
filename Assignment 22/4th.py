def sumSquare(N):
    if N==1:
        return 1
    return N**2+sumSquare(N-1)

print(sumSquare(3))