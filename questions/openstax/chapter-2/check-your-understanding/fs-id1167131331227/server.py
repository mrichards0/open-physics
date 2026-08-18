import random
def generate(data):
 while True:
  ax,ay,bx,by,cx,cy,fx,fy=[random.randint(-12,12) for _ in range(8)]; abz=ax*by-ay*bx; cfz=cx*fy-cy*fx
  if abz and cfz: break
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by,cx=cx,cy=cy,fx=fx,fy=fy); data["correct_answers"].update(abz=abz,cfz=cfz)
