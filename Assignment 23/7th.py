# def prime(n):
#     x=2
#     while n:
#         for y in range(2,x):      # Produce N numbers of fibonacci series
#             if x%y==0:
#                 break
#         else:
#             yield x
#             n-=1
#         x+=1

# for x in prime(10):
#     print(x,end=' ')

def fib():
    x=2
    while True:
        for y in range(2,x):
            if x%y==0:
                x+=1
                break
        else:
            yield x
            x+=1
it=fib()
while True:
    res=input("Wants Fibonnacci Term press Y/N:")
    if res=='y' or res=='Y':
        print(next(it),end=' ')
    else:
        break