import random
def generate(data):
 while True:
  rc,lc=random.randint(2,8),random.randint(2,8); rf,lf=random.randrange(50,251,10),random.randrange(50,251,10); net=rc*rf-lc*lf
  if net>=50: break
 data["params"].update(right_count=rc,left_count=lc,right_force=rf,left_force=lf); data["correct_answers"].update(net=net,magnitude=net)
