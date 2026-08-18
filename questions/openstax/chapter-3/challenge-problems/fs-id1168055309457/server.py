import random
def generate(data):
 while True:
  vmax=random.randint(220,360); benchmark=random.choice([80,90,96,100]); tb=random.randrange(25,61)/10; course=random.randrange(40,121)/10; vb=benchmark/3.6; vm=vmax/3.6; a=vb/tb; tm=vm/a; da=0.5*a*tm*tm; L=course*1000
  if da<L: break
 total=tm+(L-da)/vm; data["params"].update(vmax=vmax,benchmark=benchmark,tb=tb,course=course); data["correct_answers"].update(acceleration=a,tmax=tm,distance_accel=da,total=total)
