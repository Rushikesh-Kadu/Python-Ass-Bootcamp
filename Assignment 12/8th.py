N=int(input("How many terms of fibonacci series u want:"))
a,b=-1,1
while N:
    print(a+b,end=' ')
    a,b=b,a+b
    N-=1

