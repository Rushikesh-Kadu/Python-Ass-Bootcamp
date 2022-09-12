class Laptop:
    def __init__(self):
        self.brand=input("\nEnter Brand:")
        self.ram=input("Enter Ram:")
        self.cpu=input("Enter CPU:")
        self.hdd=input("Enter Hard Disk:")

    def showConfig(self):
        print("\nBrand={}\nRAM={}\nCPU={}\nHDD={}".format(self.brand,self.ram,self.cpu,self.hdd))

