f=open('cities.txt','w')
[f.write(x+'\n') for x in input("Enter City names separated by Commma:").split(',')]
f.close()