import random
def generate(data):
 vx=random.randrange(-20,51)/10; vy=random.choice([i for i in range(-5,6) if i]); ax=random.choice([i for i in range(-5,6) if i]); t=random.randrange(10,101)/10
 data["params"].update(vx0=vx,vy0=vy,ax=ax,t=t); data["correct_answers"].update(vx=vx+ax*t,vy=vy,x=vx*t+0.5*ax*t*t,y=vy*t)
