import math,random
def generate(data):
 d1,d2=random.randint(20,80),random.randint(20,80); a1,a2=random.randrange(5,86,5),random.randrange(5,86,5); x=d1*math.cos(math.radians(a1))+d2*math.cos(math.radians(a2)); y=d1*math.sin(math.radians(a1))+d2*math.sin(math.radians(a2))
 data["params"].update(d1=d1,d2=d2,a1=a1,a2=a2); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x)))
