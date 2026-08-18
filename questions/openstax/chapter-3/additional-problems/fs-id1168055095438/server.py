import random
def generate(data):
 while True:
  a=random.randrange(10,81)/10; t=random.randint(10,50); km=random.randrange(20,201)/10; d=km*1000; v0=(d-0.5*a*t*t)/t
  if v0>0: break
 data["params"].update(a=a,t=t,km=km); data["correct_answers"].update(initial=v0,final=v0+a*t)
