import math,random
def generate(data):
 while True:
  e1,e2,n1,n2,w=[random.randint(1,5) for _ in range(5)]; bx=e1+e2-w; by=n1+n2
  if bx>0: break
 block=random.choice([80,90,100,110,120]); x,y=bx*block,by*block
 data["params"].update(e1=e1,e2=e2,n1=n1,n2=n2,w=w,block=block); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x)))
