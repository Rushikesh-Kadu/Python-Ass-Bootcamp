s=input("Enter String:")
s=s.strip()
print(s)
match s:
    case s if ' ' in s:
        print("Multiword String")
    case s if ' ' not in s:
        print("Not Multiword String")
