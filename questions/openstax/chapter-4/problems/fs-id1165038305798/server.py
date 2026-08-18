import math,random
def generate(data):
 v0=random.randint(50,90); L=random.randint(70,130); A=random.randrange(20,101)/10; angle=random.randint(15,45); t=random.randrange(20,81)/10; ax=A*math.cos(math.radians(angle)); ay=A*math.sin(math.radians(angle)); vx=v0+ax*t; vy=ay*t
 data["params"].update(v0=v0,L=L,A=A,angle=angle,t=t); data["correct_answers"].update(deck=v0*v0/(2*L),ax=ax,ay=ay,y=0.5*ay*t*t,vx=vx,vy=vy,speed=math.hypot(vx,vy),x=v0*t+0.5*ax*t*t)
