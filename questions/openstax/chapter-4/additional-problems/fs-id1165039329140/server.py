import math,random
def generate(data):
 rate=random.randrange(5,51)/10; r1=random.randrange(5,21)/10; r2=r1+random.randrange(5,21)/10; r3=r2+random.randrange(5,21)/10; w=2*math.pi*rate
 data["params"].update(rate=rate,r1=r1,r2=r2,r3=r3); data["correct_answers"].update(a1=w*w*r1,a2=w*w*r2,a3=w*w*r3,ratio2=r2/r1,ratio3=r3/r1)
