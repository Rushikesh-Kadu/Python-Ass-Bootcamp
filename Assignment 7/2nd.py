print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter Ur Choice:"))
x,y=int(input("Enter 2 Numbers:")),int(input())
match choice:
    case 1:
        print("Addition :",x+y)
    case 2:
        print("Subtraction :",x-y)
    case 3:
        print("Multiplication :",x*y)
    case 4:
        print("Division :",x/y)
    case _:
        print("Invalid Choice")