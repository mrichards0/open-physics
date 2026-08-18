import math,random
def generate(data):
 x1,y1,z1,x2,y2,z2=[random.randint(-15,15) for _ in range(6)]; dx,dy,dz=x2-x1,y2-y1,z2-z1
 data["params"].update(x1=x1,y1=y1,z1=z1,x2=x2,y2=y2,z2=z2); data["correct_answers"].update(dx=dx,dy=dy,dz=dz,magnitude=math.sqrt(dx*dx+dy*dy+dz*dz))
