def check():
    x=range(int(input("Enter Range:")),int(input())+1)
    y=int(input("Enter Range:"))
    if y in x:
        print("Number in Range")
    else:
        print("Number is not in Range")

check()