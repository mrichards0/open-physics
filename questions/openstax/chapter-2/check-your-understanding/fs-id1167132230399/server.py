import math,random
def generate(data):
 while True:
  cx,cy,ax,ay=[random.randint(-50,50) for _ in range(4)]; dx,dy=-(cx+ax),-(cy+ay)
  if dx and dy and math.hypot(dx,dy)>10: break
 data["params"].update(cx=cx,cy=cy,ax=ax,ay=ay); data["correct_answers"].update(dx=dx,dy=dy,magnitude=math.hypot(dx,dy),angle=math.degrees(math.atan2(dy,dx))%360)
