try:    
    f=open('cities.txt','r')
    word=input("Enter Word to search in file:")
    for x in f.readlines():
        if x==word+'\n':
            print("Word Found")
            break
    else:
        print("Word Not Found")
except FileNotFoundError:
    print("File Doesn't Exist")
finally:
    f.close()
