import math,random
def generate(data):
 m=random.randint(3,30); a=random.randrange(0,360,10); data["params"].update(magnitude=m,angle=a); data["correct_answers"].update(x=m*math.cos(math.radians(a)),y=m*math.sin(math.radians(a)))
