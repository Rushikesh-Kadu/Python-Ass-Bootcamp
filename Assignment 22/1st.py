def sumNat(N):
    if N==1:
        return 1
    return N+sumNat(N-1)

print(sumNat(5))