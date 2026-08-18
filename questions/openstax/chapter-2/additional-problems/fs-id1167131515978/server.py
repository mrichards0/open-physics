import math,random
def generate(data):
 x,y=-random.randint(5,30),-random.randint(5,30); data["params"].update(x=x,y=y); data["correct_answers"].update(speed=math.hypot(x,y),angle=math.degrees(math.atan2(-y,-x)))
