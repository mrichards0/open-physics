import math,random
def generate(data):
 while True:
  a=random.randint(35,55); xb=random.randint(30,60); yb=random.randrange(20,51)/10; reach=random.randrange(18,36)/10; d1=random.randrange(25,int(xb*8))/10; d2=random.randrange(5,21)/10; g=random.choice([9.8,9.81]); rise=xb*math.tan(math.radians(a))-yb
  if rise>1: break
 v=math.sqrt(g*xb*xb/(2*math.cos(math.radians(a))**2*rise))
 def height(x): return x*math.tan(math.radians(a))-g*x*x/(2*v*v*math.cos(math.radians(a))**2)
 h1,h2=height(d1),height(d2); b1=h1<=reach; b2=h2<=reach
 data["params"].update(angle=a,bar_height=yb,bar_distance=xb,g=g,d1=d1,d2=d2,reach=reach,block1_yes=str(b1).lower(),block1_no=str(not b1).lower(),block2_yes=str(b2).lower(),block2_no=str(not b2).lower()); data["correct_answers"].update(speed=v,h1=h1,h2=h2)
