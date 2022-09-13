class Phone:
    def __init__(self,s,c):
        self.sms=s
        self.calling=c
    def feature(self):
        print("\nSMS={} \nCalling={}".format(self.sms,self.calling))
    
class Calculator2():    
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def multiplication(self):
        print("Multiplication :",self.num1*self.num2)

    def Division(self):
        print("Division :",self.num1/self.num2)

class SmartPhone(Phone,Calculator2):
    def __init__(self,msg,s,c,n1,n2):
        self.camera=msg
        Phone.__init__(self,s,c)
        Calculator2.__init__(self,n1,n2)
    def CameraMsg(self):
        print("Camera:",self.camera)

s1=SmartPhone("Taking Photo",'Received Msg From Anurag',"Calling shubham from yesterday",10,20)
s1.CameraMsg()
s1.feature()
s1.multiplication()
s1.Division()

