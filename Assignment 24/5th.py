class User:
    def __init__(self):
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.email=input("Enter Email:")

    def greet(self):
        try:
            print("\nWelcome ",self.name,"[Age={} Email Address={}]\n".format(self.age,self.email))
        except:
            print("\nWelcome ",self.name,"[Email Address={}]\n".format(self.email))

u1=User()
u1.greet()
del u1.age
u1.greet()