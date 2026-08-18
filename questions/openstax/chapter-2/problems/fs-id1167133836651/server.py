import math,random
def generate(data):
 while True:
  e1,e2,n1,n2,w=[random.randint(1,5) for _ in range(5)]; x=e1+e2-w; y=n1+n2
  if x>0: break
 bm=random.choice([80,90,100,110,120]); mag=math.hypot(x,y); data["params"].update(e1=e1,e2=e2,n1=n1,n2=n2,w=w,block_m=bm); data["correct_answers"].update(x=x,y=y,magnitude_blocks=mag,angle=math.degrees(math.atan2(y,x)),magnitude_m=mag*bm)
