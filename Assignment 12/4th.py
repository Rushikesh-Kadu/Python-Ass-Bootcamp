a,b=int(input("Enter 2 Numbers:")),int(input())
for x in range((a if a<b else b),(a+1 if a>b else b+1)):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')