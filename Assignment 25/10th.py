class Truecaller:
    def __init__(self):
        self.dict={}

    def fetch(self,No):
        print("\nName:",self.dict[No])

    def addEntry(self,name,number):
        self.dict[number]=name

class SmartPhone(Truecaller):
    def check(obj):
        obj.fetch(int(input("Enter Number to fetch name:")))

t1=Truecaller()
t1.addEntry('Nandu',9588732415)
s1=SmartPhone()
SmartPhone.check(t1)

