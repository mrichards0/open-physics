import random
def generate(data):
 ta=random.randrange(20,51)/10; d1=random.choice([60,100,120]); d2=random.choice([150,200,400]); T1=random.randrange(int((ta+4)*100),int((ta+12)*100))/100; T2=random.randrange(int((ta+10)*100),int((ta+40)*100))/100; v1=d1/(T1-ta/2); v2=d2/(T2-ta/2)
 data["params"].update(ta=ta,d1=d1,d2=d2,T1=T1,T2=T2); data["correct_answers"].update(v1=v1,a1=v1/ta,v2=v2)
