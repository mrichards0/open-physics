import math,random
def generate(data):
 while True:
  ax,ay,bx,by,fx,fy=[random.randint(-10,10) for _ in range(6)]; ca,cb,cf=[random.choice([-3,-2,-1,1,2,3]) for _ in range(3)]; rx,ry=ca*ax+cb*bx+cf*fx,ca*ay+cb*by+cf*fy
  if rx and ry: break
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by,fx=fx,fy=fy,ca=ca,cb=cb,cf=cf); data["correct_answers"].update(rx=rx,ry=ry,magnitude=math.hypot(rx,ry),angle=math.degrees(math.atan2(ry,rx))%360)
