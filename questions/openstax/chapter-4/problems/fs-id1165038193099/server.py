import math,random
def generate(data):
 d1=random.randint(12,30); a=random.randint(25,65); d2=random.randint(5,18); x=d1*math.cos(math.radians(a)); y=d1*math.sin(math.radians(a))-d2
 data["params"].update(d1=d1,angle=a,d2=d2); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),direction=math.degrees(math.atan2(y,x))%360)
