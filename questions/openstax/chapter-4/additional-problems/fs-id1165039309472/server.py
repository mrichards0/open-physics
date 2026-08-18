import math,random
def generate(data):
 R=random.randrange(10,151)/10; a=random.randrange(5,101)/10; t=random.randrange(10,151)/10; v=math.sqrt(a*R); w=v/R; q=w*t
 data["params"].update(radius=R,accel=a,time=t); data["correct_answers"].update(speed=v,omega=w,vx=-v*math.sin(q),vy=v*math.cos(q))
