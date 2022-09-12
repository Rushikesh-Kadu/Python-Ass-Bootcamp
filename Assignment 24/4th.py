class User:
    def __init__(self):
        self.name="Rushikesh Kadu"
        self.age=21
        self.email='rushikeshkadu066@gmail.com'

    def greet(self):
        print("\nWelcome ",self.name,"[Age={} Email Address={}]\n".format(self.age,self.email))

u1=User()
u1.greet()