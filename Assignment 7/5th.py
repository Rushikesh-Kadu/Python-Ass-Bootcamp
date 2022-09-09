num=int(input("Enter Number:"))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num<0 and num%2:
        print("Pratik Jain")
    case num if num>0 and num%2:
        print("Aditya Chaudhary")
 
