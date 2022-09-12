class User:
    def __init__(self):
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.email=input("Enter Email:")

    def greet(self):
        print("Welcome ",self.name,"[Age={} Name={}]".format(self.age,self.email))
