import math,random
def generate(data):
 R=random.randrange(5,31)/10; w=random.randrange(5,31)/10; c=random.randrange(-30,31)/10; t=random.randrange(5,41)/10; u=w*t; K=R*w; L=R*w*w
 data["params"].update(R=R,omega=w,c=c,t=t); data["correct_answers"].update(K=K,L=L,vx=-K*math.sin(u),vy=K*math.cos(u),vz=c,ax=-L*math.cos(u),ay=-L*math.sin(u),az=0)
