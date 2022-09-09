x=input("Enter String:")
y=input("Enter Alphabet:")
for s in x:
    if s!=y:
        print("String didn't contain only characters")
        break
else:
    print("String only contains characters")