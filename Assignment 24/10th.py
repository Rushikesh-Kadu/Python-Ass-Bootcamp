class Employee:
    def __init__(self):
        self.empid=0
        self.name=''
        self.sallary=0.0

    def inputField(self):
        self.empid=int(input("Enter Employee Id:"))
        self.name=input("Enter Name:")
        self.sallary=float(input("Enter Salary:"))
    
    def displayField(self):
        print('\n\nEmployee Id={} \nEmployee Name={} \nEmployee Salary={}'.format(self.empid,self.name,self.sallary))

