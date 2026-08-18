import math,random
def generate(data):
 r=random.randrange(5,31)/10; at=random.randrange(5,51)/10; t=random.randrange(10,101)/10; v=at*t; ar=v*v/r
 data["params"].update(radius=r,tangent=at,time=t); data["correct_answers"].update(speed=v,radial=ar,total=math.hypot(ar,at))
