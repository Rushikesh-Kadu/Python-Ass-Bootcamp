class User:
    def __init__(self):
        self.name=input("\nEnter Name:")
        self.age=int(input("Enter Age:"))
        self.email=input("Enter Email:")

    def greet(self):
        print("\nWelcome ",self.name,"[Age={} Email Address={}]\n".format(self.age,self.email))

u1,u2,u3=User(),User(),User()
if u1.age<u2.age and u1.age<u3.age:
    print(u1.name," is Youngest")
elif u2.age<u1.age and u2.age<u3.age:
    print(u2.name," is Youngest")
else:
    print(u3.name," is Youngest")