def cal(str):
    upp,low=0,0
    for s in str:
        if s>='a' and s<='z':
            low+=1
        elif s>='A' and s<='Z':
            upp+=1
    print("Upper case letter=",upp,"\nLower Case Letter=",low)

cal("MySirG Education Services")