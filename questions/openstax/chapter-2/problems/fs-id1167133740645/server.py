import math,random
def generate(data):
 while True:
  n1,n2,w,ne=[random.randrange(10,71,5) for _ in range(4)]; x=-w+ne/math.sqrt(2); y=n1+n2+ne/math.sqrt(2)
  if x<0: break
 data["params"].update(n1=n1,n2=n2,w=w,ne=ne); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(abs(x),y)))
