x=int(input("Enter Month Number:"))
match x:
    case month if month in (1,3,5,7,8,10,12):
        print("31 Days")
    case month if month in (2,4,6,9,11):
        print("30 Days")
    case _:
        print("Invalid Input")
   

    