import math,random
def generate(data):
 v0=random.randint(8,30); h=random.randint(30,180); g=random.choice([9.8,9.81]); t=math.sqrt(2*h/g); vy=-g*t
 data["params"].update(v0=v0,h=h,g=g); data["correct_answers"].update(time=t,vx=v0,vy=vy,speed=math.hypot(v0,vy))
