import math,random
def generate(data):
 while True:
  ds=[random.choice([1.5,2,2.5,3,3.5,4,4.5,5,6]) for _ in range(4)]; angles=random.sample(range(0,360,15),4); x=sum(d*math.cos(math.radians(a)) for d,a in zip(ds,angles)); y=sum(d*math.sin(math.radians(a)) for d,a in zip(ds,angles))
  if math.hypot(x,y)>1: break
 data["params"].update(d1=ds[0],d2=ds[1],d3=ds[2],d4=ds[3],a1=angles[0],a2=angles[1],a3=angles[2],a4=angles[3]); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x))%360)
