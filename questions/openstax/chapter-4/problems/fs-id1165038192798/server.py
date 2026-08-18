import math,random
def generate(data):
 d=random.randint(40,180); a=random.randint(20,70); t=random.randrange(10,61)/10; dx=d*math.cos(math.radians(a)); dy=d*math.sin(math.radians(a)); data["params"].update(d=d,angle=a,t=t); data["correct_answers"].update(dx=dx,dy=dy,vx=dx/t,vy=dy/t)
