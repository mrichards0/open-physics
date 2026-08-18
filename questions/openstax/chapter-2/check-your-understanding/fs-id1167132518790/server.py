import math,random
def generate(data):
 while True:
  am,bm,fm=[random.randint(5,20) for _ in range(3)]; aa,ba,fa=[random.randrange(0,360,15) for _ in range(3)]
  ax,ay=am*math.cos(math.radians(aa)),am*math.sin(math.radians(aa)); bx,by=bm*math.cos(math.radians(ba)),bm*math.sin(math.radians(ba)); fx,fy=fm*math.cos(math.radians(fa)),fm*math.sin(math.radians(fa)); gx,gy=ax+2*bx-fx,ay+2*by-fy
  if math.hypot(gx,gy)>2: break
 data["params"].update(amag=am,aangle=aa,bmag=bm,bangle=ba,fmag=fm,fangle=fa); data["correct_answers"].update(gx=gx,gy=gy,magnitude=math.hypot(gx,gy),angle=math.degrees(math.atan2(gy,gx))%360)
