import math
x=int(input("Enter Number to find square Root:"))
if(x<0):
    raise ValueError("Value can not less than zero")
s=math.sqrt(x)
print("Square Root:",s)
    