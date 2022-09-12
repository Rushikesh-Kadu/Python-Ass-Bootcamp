def co_Prime(HCF):
    def check(a,b):
        min=a if a<b else b
        for H in range(min,0,-1):
            if a%H==0 and b%H==0:
                break
        if H==1:
            print("Co-Prime")
        else:
            print("Not Co-Prime")
        HCF(a,b)
    return check

@co_Prime
def hcf(a,b):
    min=a if a<b else b
    for H in range(min,0,-1):
        if a%H==0 and b%H==0:
             print(H)
             break
hcf(70,32)
    
