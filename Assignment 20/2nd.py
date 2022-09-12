def prime(a):
    for x in range(2,a):
        if a%x==0:
            return "Not Prime"
    else:
        if a>=2:
            return "Prime"
        else:
            return "Not Prime"

print(prime(130))