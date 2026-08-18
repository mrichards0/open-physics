import math,random
def generate(data):
 f1,f2=random.randrange(2000,7001,250),random.randrange(2000,7001,250); a1,a2=random.randrange(5,31,5),random.randrange(5,31,5); f1x=f1*math.cos(math.radians(a1)); f1y=f1*math.sin(math.radians(a1)); f2x=f2*math.cos(math.radians(a2)); f2y=-f2*math.sin(math.radians(a2)); rx,ry=f1x+f2x,f1y+f2y
 data["params"].update(f1=f1,f2=f2,a1=a1,a2=a2); data["correct_answers"].update(f1x=f1x,f1y=f1y,f2x=f2x,f2y=f2y,rx=rx,ry=ry,magnitude=math.hypot(rx,ry),angle=math.degrees(math.atan2(ry,rx)))
