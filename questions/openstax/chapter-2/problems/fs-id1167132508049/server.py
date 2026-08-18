import math,random
def generate(data):
 w,n=random.randint(5,40),random.randint(5,40); x,y=-w,n; data["params"].update(west=w,north=n); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),angle=math.degrees(math.atan2(y,x))%360)
