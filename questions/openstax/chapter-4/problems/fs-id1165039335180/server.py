import math, random
def generate(data):
    ship=random.randrange(30,121)/10; current=random.randrange(5,51)/10; angle=random.randint(10,80)
    vx=current*math.cos(math.radians(angle)); vy=ship+current*math.sin(math.radians(angle))
    data["params"].update(ship=ship,current=current,angle=angle)
    data["correct_answers"].update(vx=vx,vy=vy,speed=math.hypot(vx,vy),direction=math.degrees(math.atan2(vx,vy)))
