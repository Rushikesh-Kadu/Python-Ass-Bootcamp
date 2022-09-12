class Laptop:
    def __init__(self):
        self.brand=input("\nEnter Brand:")
        self.ram=int(input("Enter Ram:"))
        self.cpu=input("Enter CPU:")
        self.hdd=input("Enter Hard Disk:")

    def showConfig(self):
        print("\nBrand={}\nRAM={}\nCPU={}\nHDD={}".format(self.brand,self.ram,self.cpu,self.hdd))


l1,l2,l3=Laptop(),Laptop(),Laptop()
l1.showConfig()
l2.showConfig()
l3.showConfig()

t=(l1,l2,l3)
l=[]
list=sorted([t[0].ram,t[1].ram,t[2].ram])
for x in range(0,3):
    for y in range(0,3):
     if list[x]==t[y].ram:
        l.append(t[y])
        break
l[0].showConfig()
l[1].showConfig()
l[2].showConfig()