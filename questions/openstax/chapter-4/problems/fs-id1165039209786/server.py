import math, random
def generate(data):
    rain=random.randrange(20,101)/10; car=random.randrange(80,351)/10
    data["params"].update(rain=rain,car=car)
    data["correct_answers"].update(vx=-car,vy=-rain,speed=math.hypot(car,rain),angle=math.degrees(math.atan2(rain,car)))
