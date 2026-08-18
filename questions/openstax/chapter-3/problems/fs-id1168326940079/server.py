import random
def generate(data):
 while True:
  x0=random.randint(-20,20); v=random.choice([i for i in range(-10,11) if i]); crossing=-x0/v
  if crossing>0: break
 t1=random.randint(0,8); t2=t1+random.randint(1,8); data["params"].update(x0=x0,v=v,t1=t1,t2=t2); data["correct_answers"].update(crossing=crossing,displacement=v*(t2-t1))
