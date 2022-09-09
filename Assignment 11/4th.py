N=int(input("How many odd numbers sum u want:"))
s=0
while N:
    s=s+(N*2-1)
    N-=1
print(s)