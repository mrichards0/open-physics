import math,random
def generate(data):
 x=random.choice([i for i in range(-10,11) if i]); y=random.choice([i for i in range(-10,11) if i]); data["params"].update(x=x,y=y); data["correct_answers"].update(r=math.hypot(x,y),angle=math.degrees(math.atan2(y,x))%360)
