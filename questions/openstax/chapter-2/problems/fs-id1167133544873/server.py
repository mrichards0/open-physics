import math,random
def generate(data):
 r=random.choice([2,3,4,5,5.5,6,7.5,8,10]); a=random.randrange(0,360,15); data["params"].update(r=r,angle=a); data["correct_answers"].update(x=r*math.cos(math.radians(a)),y=r*math.sin(math.radians(a)))
