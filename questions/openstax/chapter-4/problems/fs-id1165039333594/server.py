import math, random
def generate(data):
    bike=random.randrange(50,251)/10; apparent=random.randrange(80,351)/10; q=math.sqrt(2)
    vx=(bike+apparent)/q; vy=(apparent-bike)/q
    direction=math.degrees(math.atan2(vy,vx))%360
    data["params"].update(bike=bike,apparent=apparent)
    data["correct_answers"].update(vx=vx,vy=vy,speed=math.hypot(vx,vy),direction=direction)
