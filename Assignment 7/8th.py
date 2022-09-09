x=input("Enter 1st String:")
y=input("Enter 2nd String:")
match (x,y):
    case (x,y) if x<y:
        print("First string Comes before the second string")
    case (x,y) if x>y:
        print("First String comes after the second String")
    case (x,y) if x==y:
        print("String is Identical")