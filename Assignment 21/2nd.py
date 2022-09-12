def revNat(N):
    if N>0:
        print(N)
        revNat(N-1)

revNat(10)