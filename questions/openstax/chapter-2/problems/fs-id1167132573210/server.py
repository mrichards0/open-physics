import random
def generate(data):
 while True:
  dx,dy,bx,by=[random.randint(-8,8) for _ in range(4)]
  if dx*by-dy*bx: break
 a,b=random.choice([i for i in range(-5,6) if i]),random.choice([i for i in range(-5,6) if i]); ax=-(a*dx+b*bx); ay=-(a*dy+b*by)
 data["params"].update(dx=dx,dy=dy,bx=bx,by=by,ax=ax,ay=ay); data["correct_answers"].update(a=a,b=b)
