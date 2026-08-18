import random
def generate(data):
 while True:
  dx,dy,dz,gx,gy=[random.choice([i for i in range(-6,7) if i]) for _ in range(5)]
  if dz and (-dx*gx-dy*gy)%dz==0:
   gz=(-dx*gx-dy*gy)//dz
   if gz and abs(gz)<=20: break
 data["params"].update(dx=dx,dy=dy,dz=dz,gx=gx,gy=gy,gz=gz); data["correct_answers"]["dot"]=0
