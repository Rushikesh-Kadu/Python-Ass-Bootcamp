def even(N):
    if N>0:
        even(N-1)
        print(N*2)

even(10)