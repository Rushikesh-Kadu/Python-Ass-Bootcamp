while 1:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input("Enter ur Choice:"))
    a=int(input("Enter 1st Number:"))
    b=int(input("Enter 2nd Number:"))
    try:
        match choice:
            case 1:
                print("Addition is:",a+b)
            case 2:
                print("Subtraction is:",a-b)
            case 3:
                print("Multiplication is",a*b)
            case 4:
                print("Division is:",a/b)
    except ZeroDivisionError:
        print("\nEnter Valid Data")
        continue
    except TypeError:
        print("\nEnter Valid Data")
        continue
    except ValueError:
        print("\nEnter Valid Data")
        continue
    except:
        print("\nEnter Valid Data")
        continue
    finally:
        if("NO"==input("\nWants to calculate again(Yes/No):").upper()):
            break
    