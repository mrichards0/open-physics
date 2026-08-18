import random
def generate(data):
 while True:
  kmh=random.randrange(400,1010,10)/10; v0=kmh/3.6; t=random.randrange(10,51)/10; d=random.randrange(200,1001)/10
  if d>v0*t+2: break
 a=2*(d-v0*t)/(t*t); data["params"].update(kmh=kmh,d=d,t=t); data["correct_answers"].update(acceleration=a,speed=v0+a*t)
