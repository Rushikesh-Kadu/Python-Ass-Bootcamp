year=int(input("Enter Year:"))
match year:
    case year if year%400==0:
        print("Century Leap Year")
    case year if year%100!=0 and year%4!=0:
        print("Non century non Leap Year")
    case year if year%100==0 and year%400!=0:
        print("Century non leap year")
    case year if year%4==0:
        print("Non Century Leap Year")
    