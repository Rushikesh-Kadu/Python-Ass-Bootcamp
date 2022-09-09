tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
l,z,i=[],[],0
for x in tuple1:
    l.append(x[1])
l.sort()
while i<len(tuple1):
    for x in tuple1:
        if l[i]==x[1]:
            z.append(x)
    i+=1
z=tuple(z)
print(z)