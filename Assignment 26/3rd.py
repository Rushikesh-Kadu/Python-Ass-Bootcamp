class User_Account:
    def __init__(self,ui,b):
        self.userid=ui
        self.balance=b
    def __add__(o1,o2):
        #print(o1.userid)
        u=User_Account(0,0)
        u.userid=o1.userid+o2.userid
        u.balance=o1.balance+o2.balance
        return u

    def __str__(self):
        return str(self.userid)+"   "+str(self.balance)

u1=User_Account(101,2000)
u2=User_Account(102,3000)
u3=User_Account(103,4000)
u4=User_Account(104,5000)
u5=User_Account(105,6000)
u6=User_Account(0,0)
u6=u1+u2+u3+u4+u5           #__add__(u1,u2,u3,u4,u5)
print(u6)                   #__str__(u6)  //Which returns string & print()
                            #method prints that string