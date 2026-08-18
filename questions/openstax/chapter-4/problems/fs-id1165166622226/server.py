import math,random
def generate(data):
 plane=random.randint(80,180); rel=random.randint(150,400); h=random.randint(300,1500); g=random.choice([9.8,9.81]); vx=plane+rel; t=math.sqrt(2*h/g); vy=-g*t
 data["params"].update(plane=plane,relative=rel,h=h,g=g); data["correct_answers"].update(launch=vx,time=t,range=vx*t,vy=vy,speed=math.hypot(vx,vy))
