import math,random
def generate(data):
 while True:
  first=random.randrange(300,801)/100; a1=random.randrange(25,51); a2=random.randrange(55,81); a3=random.randrange(15,41)
  t1=math.radians(a1); t2=math.radians(90+a2); tmp=math.radians(270+a3); ux,uy=math.cos(t2),math.sin(t2); vx,vy=math.cos(tmp),math.sin(tmp); bx,by=-first*math.cos(t1),-first*math.sin(t1); det=ux*vy-uy*vx
  np=(bx*vy-by*vx)/det; pm=(ux*by-uy*bx)/det
  if np>0 and pm>0: break
 data["params"].update(first=first,a1=a1,a2=a2,a3=a3); data["correct_answers"].update(npnmi=np,npkm=1.852*np,mpnmi=pm,mpkm=1.852*pm)
