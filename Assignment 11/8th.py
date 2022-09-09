N=int(input("Enter Number:"))
s=0
while N:
    r=N%10
    s=s+r
    N//=10
print(s)