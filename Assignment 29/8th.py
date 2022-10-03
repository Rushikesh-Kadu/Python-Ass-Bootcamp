def copy(fileName):
    f=open(fileName,'r')
    text=f.read()
    f1=open('1'+fileName,'w')
    f1.write(text)
    f1.close()
    f.close()
    print("Copy Created Successfully")

copy('cities.txt')
