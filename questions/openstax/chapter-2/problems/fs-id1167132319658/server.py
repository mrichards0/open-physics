import math,random
def generate(data):
 while True:
  ax,ay,bx,by=[random.choice([i for i in range(-10,11) if i]) for _ in range(4)]
  if (ax,ay)!=(bx,by): break
 data["params"].update(ax=ax,ay=ay,bx=bx,by=by); data["correct_answers"].update(distance=math.hypot(bx-ax,by-ay),ar=math.hypot(ax,ay),aa=math.degrees(math.atan2(ay,ax))%360,br=math.hypot(bx,by),ba=math.degrees(math.atan2(by,bx))%360)
