import math,random
def generate(data):
 while True:
  kmh=random.randint(40,80); v=kmh/3.6; a=random.randint(15,40); drop=random.randint(60,150); gorge=random.randint(50,100); g=random.choice([9.8,9.81]); vd=v*math.sin(math.radians(a)); t=(-vd+math.sqrt(vd*vd+2*g*drop))/g; travel=v*math.cos(math.radians(a))*t; margin=travel-gorge
  if margin<0: break
 data["params"].update(kmh=kmh,angle=a,drop=drop,gorge=gorge,g=g); data["correct_answers"].update(time=t,travel=travel,margin=margin)
