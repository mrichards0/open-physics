import math,random
def generate(data):
 v=random.randint(8,30); a=random.randint(20,70); g1=random.randrange(20,121)/10; g2=random.randrange(10,101)/10; common=v*v*math.sin(math.radians(2*a)); r1=common/g1; r2=common/g2
 data["params"].update(v=v,angle=a,g1=g1,g2=g2); data["correct_answers"].update(r1=r1,r2=r2,ratio=r2/r1)
