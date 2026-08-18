import math, random
def generate(data):
    current=random.randrange(10,81)/10; boat=random.randrange(40,151)/10; angle=random.randint(15,75); width=random.randint(300,2500)
    vx=current-boat*math.cos(math.radians(angle)); vy=boat*math.sin(math.radians(angle)); t=width/vy
    data["params"].update(current=current,boat=boat,angle=angle,width=width)
    data["correct_answers"].update(vx=vx,vy=vy,speed=math.hypot(vx,vy),time=t,drift=vx*t)
