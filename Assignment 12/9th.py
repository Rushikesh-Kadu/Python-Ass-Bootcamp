a,b=int(input("Enter 2 Numbers:")),int(input())
for L in range((a if a>b else b),(a*b)+1):
    if L%a==0 and L%b==0:
        print("LCM is: ",L)
        break