import math,random
def generate(data):
 while True:
  v0=random.randint(18,35); d=random.randrange(5,31)/100; station=random.randint(120,300); length=random.randint(70,180)
  if v0*v0>2*d*(station+length)+25: break
 vn=math.sqrt(v0*v0-2*d*station); vr=math.sqrt(v0*v0-2*d*(station+length)); data["params"].update(v0=v0,decel=d,station=station,length=length); data["correct_answers"].update(vnose=vn,tnose=(v0-vn)/d,vrear=vr,trear=(v0-vr)/d)
