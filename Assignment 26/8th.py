t=int(input())
for y in range(t):
    a,b=[int(x) for x in input().split(' ')]
    try:
        z=a//b
        print(z)
    except:
        print("Error Code:",exception)
