import math,random
def generate(data):
 while True:
  bottom=random.randrange(30,151)/10; window=random.randrange(10,41)/10; dt=random.randrange(20,81)/100; g=random.choice([9.8,9.81]); vb=(window+0.5*g*dt*dt)/dt
  if vb-g*dt>0: break
 v0=math.sqrt(vb*vb+2*g*bottom); data["params"].update(bottom=bottom,window=window,dt=dt,g=g); data["correct_answers"]["velocity"]=v0
