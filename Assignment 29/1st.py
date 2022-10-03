f=open('File.txt','w')
if f.mode=='r':
    print("Read Only")
else:
    print("Not just Read Only")
if f.closed:
    print("File Is Closed")
else:
    print("File is Opened")
print("Mode:",f.mode)
print("Name of File:",f.name)
f.close()