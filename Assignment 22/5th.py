def quabe(N):
    if N==1:
        return 1
    return N**3+quabe(N-1)