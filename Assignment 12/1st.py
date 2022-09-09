x=int(input("Enter Number:"))
s=0
while x:
    r=x%10
    s=s*10+r
    x//=10
print(s)