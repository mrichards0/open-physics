import math,random
def generate(data):
 r=random.randint(60,300); speed=random.randrange(300,1001)/10; rate=random.randrange(10,151)/10; v=speed/3.6; at=-rate/3.6; ar=v*v/r
 data["params"].update(radius=r,speed=speed,rate=rate); data["correct_answers"].update(radial=ar,tangent=at,total=math.hypot(ar,at))
