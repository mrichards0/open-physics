import math,random
def generate(data):
 d=random.choice([3,5,7.5,10,12,15,20]); a=random.randrange(10,81,5); data["params"].update(distance=d,angle=a); data["correct_answers"].update(east=d*math.sin(math.radians(a)),north=d*math.cos(math.radians(a)))
