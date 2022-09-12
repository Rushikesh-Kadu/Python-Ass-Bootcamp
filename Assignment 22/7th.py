def sumDigit(N):
    if N==0:
        return 0
    return N%10+sumDigit(N//10)

print(sumDigit(9872))