class User:
    def __init__(self):
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.email=input("Enter Email:")

    def greet(self):
        print("\nWelcome ",self.name,"[Age={} Email Address={}]\n".format(self.age,self.email))

u1=User()
u1.greet()
u2=User()
u2.greet()