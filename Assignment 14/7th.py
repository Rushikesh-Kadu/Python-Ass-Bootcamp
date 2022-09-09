x=[1,4.5,"Hello",False,3+5j,4.5,11,99,0,True]
y=[]
for a in x:
    if(type(a)==int):
        y.append(a)
print(y)