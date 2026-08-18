import math,random
def generate(data):
 fx=random.choice([i for i in range(-9000,9001,250) if i]); fy=random.choice([i for i in range(-9000,9001,250) if i]); data["params"].update(fx=fx,fy=fy); data["correct_answers"].update(magnitude=math.hypot(fx,fy),angle=math.degrees(math.atan2(fy,fx))%360)
