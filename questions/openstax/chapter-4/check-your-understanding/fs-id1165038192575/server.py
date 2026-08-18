import random
def generate(data):
 c=random.randrange(5,41)/10; tm=random.randint(2,8); delta=random.randint(1,tm); t1=tm-delta; t2=tm+delta; y=random.randint(-10,10)
 data["params"].update(c=c,tm=tm,t1=t1,t2=t2,y=y); data["correct_answers"].update(vix=3*c*tm*tm,viy=0,vax=c*(t2**3-t1**3)/(t2-t1),vay=0)
