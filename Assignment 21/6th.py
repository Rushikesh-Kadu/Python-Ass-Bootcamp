def even(N):
    if N>0:
        print(N*2)
        even(N-1)
even(10)