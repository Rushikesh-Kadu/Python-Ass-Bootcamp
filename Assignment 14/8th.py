l1=[1,2,3,4,5,6,4,5,3,2,1,1,4,7,8,11,21,00,19]
index=0
while index<len(l1):
    if l1.index(l1[index])==index:
        print(l1[index],"   ",l1.count(l1[index]))
    index+=1