import random
def generate(data):
 while True:
  d=random.randint(200,500); vi=random.randrange(80,151)/10; a=random.randrange(20,101)/100; ta=random.randrange(30,101)/10; gap=random.randrange(20,101)/10; vr=random.randrange(80,151)/10; vf=vi+a*ta; da=vi*ta+0.5*a*ta*ta
  if da>=d: continue
  tw=ta+(d-da)/vf; tr=(d-gap)/vr
  if tr>tw: break
 data["params"].update(d=d,vi=vi,a=a,ta=ta,gap=gap,vr=vr); data["correct_answers"].update(vf=vf,saved=d/vi-tw,difference=tr-tw,behind=vr*(tr-tw))
