import math,random
def generate(data):
 dx=random.choice([i for i in range(-12,13) if i]); dy=random.choice([i for i in range(-12,13) if i])
 data["params"].update(dx=dx,dy=dy); data["correct_answers"].update(magnitude=math.hypot(dx,dy),angle=math.degrees(math.atan2(dy,dx))%360)
