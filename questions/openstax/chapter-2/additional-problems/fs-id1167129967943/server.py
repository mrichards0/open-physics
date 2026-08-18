import math,random
def generate(data):
 while True:
  n=random.randrange(50,151,5); e=random.randrange(100,251,5); g=random.randrange(40,121,5); a=random.randrange(15,61,5); c=random.randrange(120,251,5); x=e+g*math.cos(math.radians(a)); y=n+g*math.sin(math.radians(a))-c
  if y<0: break
 rx,ry=-x,-y; data["params"].update(north=n,east=e,grouper=g,angle=a,current=c); data["correct_answers"].update(distance=math.hypot(rx,ry),angle=math.degrees(math.atan2(ry,-rx)))
