import math,random
def generate(data):
 vx=random.randint(-30,30); vy=random.randint(-30,30); vz=random.randint(-15,15)
 if vx==vy==vz==0: vx=10
 data["params"].update(vx=vx,vy=vy,vz=vz); data["correct_answers"]["speed"]=math.sqrt(vx*vx+vy*vy+vz*vz)
