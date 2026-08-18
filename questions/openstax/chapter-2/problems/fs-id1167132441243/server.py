import math,random
def generate(data):
 x0,y0,z0=[random.randint(0,8) for _ in range(3)]
 while True:
  x1,y1,z1=[random.randint(0,8) for _ in range(3)]
  if (x1,y1,z1)!=(x0,y0,z0): break
 dx,dy,dz=x1-x0,y1-y0,z1-z0; data["params"].update(x0=x0,y0=y0,z0=z0,x1=x1,y1=y1,z1=z1); data["correct_answers"].update(dx=dx,dy=dy,dz=dz,magnitude=math.sqrt(dx*dx+dy*dy+dz*dz))
