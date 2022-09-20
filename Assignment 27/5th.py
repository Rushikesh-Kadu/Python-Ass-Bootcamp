x=int(input("Enter 1st Number:"))
y=int(input("Enter 2nd Number:"))
try:
    z=x+y
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Type Error")
except :
    print("Enter Correct Data!!!")