def fib(N):
    if N==1 or N==2:
        return N-1
    return fib(N-1)+fib(N-2)

print(fib(6))