import math,random
def generate(data):
 while True:
  x=random.randrange(60,201)/10; h=random.randrange(150,351)/100; a=random.randint(20,50); g=random.choice([9.8,9.81]); rise=x*math.tan(math.radians(a))-h
  if rise>0: break
 v=math.sqrt(g*x*x/(2*math.cos(math.radians(a))**2*rise)); data["params"].update(x=x,h=h,angle=a,g=g); data["correct_answers"].update(speed=v,time=x/(v*math.cos(math.radians(a))))
