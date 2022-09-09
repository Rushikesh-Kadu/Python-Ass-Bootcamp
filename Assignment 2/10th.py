from datetime import *

date=datetime.now()
time=datetime.today()
print(date.day,date.month,date.year,sep='-')
print(date.strftime("%I:%M %p"))