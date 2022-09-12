class Profile:
    def __init__(self):
        self.name=input("Enter Name:")
        self.email=input("Enter Email:")
        self.age=int(input("Enter Age:"))
        self.platform=input("Enter Platform:")

    def access(self):
        print("\nName={} \nEmail={} \nAge={} \nPlatform={}".format(self.name,self.email,self.age,self.platform))