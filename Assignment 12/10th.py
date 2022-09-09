a,b=int(input("Enter 2 Numbers:")),int(input())
for H in range((a if a<b else b),0,-1):
    if a%H==0 and b%H==0:
        print("HCF is:",H)
        break