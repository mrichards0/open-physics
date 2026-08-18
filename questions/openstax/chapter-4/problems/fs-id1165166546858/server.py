import math,random
def generate(data):
 while True:
  y0=random.randrange(120,221)/100; yf=random.randrange(250,401)/100; x=random.randrange(400,901)/100; a=random.randint(45,70); g=random.choice([9.8,9.81]); dy=yf-y0; den=2*math.cos(math.radians(a))**2*(x*math.tan(math.radians(a))-dy)
  if den>0: break
 v=math.sqrt(g*x*x/den); data["params"].update(y0=y0,yf=yf,x=x,angle=a,g=g); data["correct_answers"].update(speed=v,time=x/(v*math.cos(math.radians(a))))
