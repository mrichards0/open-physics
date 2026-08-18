import math,random
def generate(data):
 d1=random.randrange(50,151)/10; a=random.randint(20,70); t1=random.randrange(5,21)/10; d2=random.randrange(50,201)/10; t2=random.randrange(5,31)/10; dx=d1*math.cos(math.radians(a)); dy=d1*math.sin(math.radians(a))+d2; total=t1+t2
 data["params"].update(d1=d1,angle=a,t1=t1,d2=d2,t2=t2); data["correct_answers"].update(dx=dx,dy=dy,dmag=math.hypot(dx,dy),vx=dx/total,vy=dy/total,vmag=math.hypot(dx,dy)/total)
