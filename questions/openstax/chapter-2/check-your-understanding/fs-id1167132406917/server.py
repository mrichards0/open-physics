import random
def generate(data):
 x0,y0=random.randint(3,15),random.randint(3,15)
 while True:
  x1,y1=random.randint(0,18),random.randint(0,18)
  if x1!=x0 and y1!=y0: break
 data["params"].update(x0=x0,y0=y0,x1=x1,y1=y1); data["correct_answers"].update(dx=x1-x0,dy=y1-y0)
