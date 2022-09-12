dict1={1: 'Sandeep', 2: 'Saurabh', 3: 'Samir', 4: 'Sharukh'}
dict2={5:'Sawstik',6:'Ganesha'}
dict3={}
for x in dict1:
    dict3[x]=dict1[x]
for x in dict2:
    dict3[x]=dict2[x]
print(dict3)