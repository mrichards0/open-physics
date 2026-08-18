import math,random
def generate(data):
 r=random.randrange(30,301)/10; v=random.randrange(50,501)/10; at=random.randrange(10,201)/10; ar=v*v/r
 data["params"].update(radius=r,speed=v,tangent=at); data["correct_answers"].update(radial=ar,tangent=at,total=math.hypot(ar,at))
