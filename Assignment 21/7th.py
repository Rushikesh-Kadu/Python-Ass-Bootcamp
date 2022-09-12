def square(N):
    if N>0:
        square(N-1)
        print(N**2)

square(10)