x,y=int(input("Enter 2 Numbers:")),int(input())
for H in range((x if x<y else y),0,-1):
    if x%H==0 and y%H==0:
        break
if H==1:
    print("Co-Prime")
else:
    print("Not Co-Prime")


