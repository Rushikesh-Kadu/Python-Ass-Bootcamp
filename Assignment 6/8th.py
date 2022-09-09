a,b,c=int(input("Enter value of a,b and c of quadratic equation:")),int(input()),int(input())
d=b**2-2*a*c
if d>0:
    print("Real and Distinct")
elif d==0:
    print("Real and Equal")
else:
    print("Imaginary")
    