a,b,c=int(input("Enter 3 Number:")),int(input()),int(input())
x=[a,b,c]
x.remove(max(x))
match (a,b,c):
    case (a,b,c) if max((a,b,c))**2==x[0]**2+x[1]**2:
        print("Right angled Triangle")
    case (a,b,c) if a is b and a is c:
        print("Quadrilateral Triangle")
    case (a,b,c) if a==b or a==c or b==c:
        print("Isosceles Triangle")