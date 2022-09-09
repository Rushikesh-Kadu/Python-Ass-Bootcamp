N=int(input("How many natural numbers sum u want:"))
s=0
while N:
    s=s+N**2
    N-=1
print(s)