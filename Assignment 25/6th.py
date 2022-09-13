class Calculator:
    def __init__(self):
        self.num1=int(input("Enter 1st Number:"))
        self.num2=int(input("Enter 2nd Number:"))

    def addition(self):
        print("Addition :",self.num1+self.num2)

    def subtraction(self):
        print("Subtraction :",self.num1+self.num2)

class Calculator2(Calculator):
    def multiplication(self):
        print("Multiplication :",self.num1*self.num2)

    def Division(self):
        print("Division :",self.num1/self.num2)

a1=Calculator2()
a1.addition()
a1.multiplication()
        