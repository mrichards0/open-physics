import math,random
def generate(data):
 while True:
  ax,ay,bx,by,fx,fy=[random.randint(-12,12) for _ in range(6)]; gx=ax+2*bx-fx; gy=ay+2*by-fy
  if gx and gy: break
 angle=math.degrees(math.atan2(gy,gx))%360
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by,fx=fx,fy=fy); data["correct_answers"].update(gx=gx,gy=gy,magnitude=math.hypot(gx,gy),angle=angle)
