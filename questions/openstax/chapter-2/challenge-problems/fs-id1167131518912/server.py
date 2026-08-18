import random
def generate(data):
 while True:
  ax,ay,bx,by=[random.randint(-12,12) for _ in range(4)]
  if ax!=bx or ay!=by: break
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by); data["correct_answers"].update(cx=(bx-ax)/2,cy=(by-ay)/2,ratio=0.5)
