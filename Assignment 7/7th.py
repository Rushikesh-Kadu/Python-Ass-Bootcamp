x=int(input("Enter Number:"))
match x:
    case x if x>0:
        print("Positive")
    case x if x<0:
        print("Negative")
    case x if x==0:
        print("Zero")