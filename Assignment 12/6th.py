N=int(input("Enter Number:"))
a=1
while N:
    a+=1
    for x in range(2,a):
        if a%x==0:
            break
    else:
        print(a,end=' ')
        N-=1
