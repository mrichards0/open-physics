import math,random
def generate(data):
 e=random.randrange(20,121)/10; m=random.randrange(50,181)/10; a=random.randint(10,50); w=random.randrange(20,121)/10; x=e-m*math.sin(math.radians(a))-w; y=m*math.cos(math.radians(a))
 data["params"].update(east=e,middle=m,angle=a,west=w); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle_out=math.degrees(math.atan2(-x,y)))
