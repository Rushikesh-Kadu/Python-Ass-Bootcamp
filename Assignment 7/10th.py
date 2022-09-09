sentence=input("Enter Sentence:")
match sentence:
    case sentence if 'yellow' in sentence:
        print("Monday")
    case sentence if 'blue' in sentence:
        print("Tuesday")
    case sentence if 'orange' in sentence:
        print("Wednesday")
    case sentence if 'white' in sentence:
        print("Thursday")
    case sentence if 'black' in sentence:
        print("Friday")
    case sentence if 'red' in sentence:
        print("Saturday")
    case _:
        print("Sunday")