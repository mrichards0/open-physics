import math,random
def generate(data):
 h=random.randrange(50,201)/100; r=random.randrange(100,601)/100; g=random.choice([9.8,9.81]); t=math.sqrt(2*h/g); vx=r/t; vy=-g*t
 data["params"].update(h=h,range=r,g=g); data["correct_answers"].update(time=t,launch=vx,vy=vy,impact=math.hypot(vx,vy))
