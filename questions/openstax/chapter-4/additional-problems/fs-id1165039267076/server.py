import math,random
def generate(data):
 R=random.randrange(10,101)/10; w=random.randrange(5,61)/10; t=random.randrange(10,201)/10; q=w*t; c=math.cos(q); s=math.sin(q)
 data["params"].update(radius=R,omega=w,time=t); data["correct_answers"].update(x=R*c,y=R*s,vx=-R*w*s,vy=R*w*c,ax=-R*w*w*c,ay=-R*w*w*s)
