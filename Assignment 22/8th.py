# def bin(N):
#     if N>0:
#         print(N%2,end='')
#         bin(N//2)
# bin(9)


def bin(N):
    if N==0:
        return ''  
    return str(N%2)+bin(N//2)

x=int(bin(9))
print(x,type(x))
