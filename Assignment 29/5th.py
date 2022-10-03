f=open('cities.txt','a')
[f.write(x+'\n') for x in input("Enter Cities to append in File:").split(',')]
f.close()