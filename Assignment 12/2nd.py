x=int(input("Enter Number:"))
y=2
while y<x:
    if(x%y==0):
        break
    y+=1
if y==x:
    print("Prime")
else:
    print("Not Prime")