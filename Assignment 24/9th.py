class School:
    def __init__(self):
        School.std='10th'
        self.stuName=input("Enter Name:")
        self.rollNo=int(input("Enter Roll No:"))
        self.mobileNo=int(input("Enter Number:"))

    def showData(self):
        print("\nSchool={} \nStudent Name={} \nRoll Number={} \nMobile Number={}".format(self.std,self.stuName,self.rollNo,self.mobileNo))

s1=School()
s1.showData()