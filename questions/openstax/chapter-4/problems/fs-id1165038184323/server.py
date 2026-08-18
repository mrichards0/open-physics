import math,random
def generate(data):
 x1=random.randint(150,350); y1=random.randint(-30,30); length=random.randint(100,250); angle=random.randint(-50,80); x2=length*math.cos(math.radians(angle)); y2=length*math.sin(math.radians(angle)); x=x1+x2; y=y1+y2
 data["params"].update(x1=x1,y1=y1,x2=x2,y2=y2); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x))%360)
