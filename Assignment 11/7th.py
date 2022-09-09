N=int(input("Enter Number:"))
count=0
while N:
    N//=10
    count+=1
print(count)