import math,random
def generate(data):
 vx=random.randint(3,30); vy=random.randint(3,30); speed=math.hypot(vx,vy)
 data["params"].update(vx=vx,vy=vy,speed=speed); data["correct_answers"].update(ux=vx/speed,uy=vy/speed,angle=math.degrees(math.atan2(vy,vx)))
