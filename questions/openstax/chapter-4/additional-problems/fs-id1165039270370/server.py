import math,random
def generate(data):
 r=random.randrange(5,31)/10; c1=random.randint(1,8)*1e5; c2=random.randint(1,8)*1e4; t=random.randrange(10,101)/10; light=3e8; v=c1+c2*t*t; at=2*c2*t; ar=v*v/(r*1000)
 data["params"].update(radius=r,c1=c1,c2=c2,time=t,light=light); data["correct_answers"].update(tangent=at,radial=ar,total=math.hypot(at,ar),unphysical=math.sqrt((light-c1)/c2))
