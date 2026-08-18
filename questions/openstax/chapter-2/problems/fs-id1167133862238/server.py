import math,random
def generate(data):
 while True:
  vals=[random.randint(-10,10) for _ in range(8)]; coeff=[random.choice([-4,-3,-2,-1,0,1,2,3]) for _ in range(4)]; ax,ay,cx,cy,dx,dy,fx,fy=vals; ca,cc,cd,cf=coeff; x=ca*ax+cc*cx+cd*dx+cf*fx; y=ca*ay+cc*cy+cd*dy+cf*fy
  if x or y: break
 data["params"].update(ax=ax,ay=ay,cx=cx,cy=cy,dx=dx,dy=dy,fx=fx,fy=fy,ca=ca,cc=cc,cd=cd,cf=cf); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y))
