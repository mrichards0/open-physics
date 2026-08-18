import math,random
def generate(data):
 n=random.randrange(20,81)/10; e=random.randrange(10,61)/10; data["params"].update(north=n,east=e); data["correct_answers"].update(vx=e,vy=n,speed=math.hypot(e,n),angle=math.degrees(math.atan2(e,n)))
