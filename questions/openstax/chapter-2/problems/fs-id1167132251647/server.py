import math,random
def generate(data):
 while True:
  ax,ay,bx,by=[random.randint(-12,12) for _ in range(4)]; sx,sy=ax+bx,ay+by; dx,dy=ax-bx,ay-by
  if sx and sy and dx and dy: break
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by); data["correct_answers"].update(sx=sx,sy=sy,smag=math.hypot(sx,sy),sangle=math.degrees(math.atan2(sy,sx))%360,dx=dx,dy=dy,dmag=math.hypot(dx,dy),dangle=math.degrees(math.atan2(dy,dx))%360)
