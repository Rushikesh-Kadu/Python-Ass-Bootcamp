a=int(input("Enter Number:"))
while 1:
    a+=1
    for x in range(2,a):
        if a%x==0:
            break
    else:
        print("Next Prime:",a)
        break
