import math,random
def generate(data):
 while True:
  ds=[random.choice([1.5,2,2.5,3,4,5,6,7]) for _ in range(5)]; aa=random.sample(range(0,360,15),5); x=sum(d*math.cos(math.radians(a)) for d,a in zip(ds,aa)); y=sum(d*math.sin(math.radians(a)) for d,a in zip(ds,aa))
  if math.hypot(x,y)>1: break
 data["params"].update(**{f"d{i+1}":ds[i] for i in range(5)},**{f"a{i+1}":aa[i] for i in range(5)}); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x))%360)
