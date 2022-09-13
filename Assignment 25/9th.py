class Truecaller:
    def __init__(self):
        self.dict={}

    def fetch(self,No):
        print("\nName:",self.dict[No])

    def addEntry(self,name,number):
        self.dict[number]=name

t1=Truecaller()
t1.addEntry('Sandeep',9055607080)
t1.addEntry('Suarabh',7083845677)
t1.fetch(7083845677)
