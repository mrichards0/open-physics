import math,random
def generate(data):
 h1,h2=random.randrange(1500,4001,250),random.randrange(1500,4001,250); e1,e2=random.randrange(5,21,5),random.randrange(5,21,5); az1=random.choice([120,135,150,165,195,210,225,240]); q1=h1/math.tan(math.radians(e1)); q2=h2/math.tan(math.radians(e2)); x1=q1*math.cos(math.radians(az1)); y1=q1*math.sin(math.radians(az1)); x2=-q2; y2=0; distance=math.sqrt((x1-x2)**2+(y1-y2)**2+(h1-h2)**2)
 data["params"].update(h1=h1,h2=h2,e1=e1,e2=e2,az1=az1); data["correct_answers"].update(x1=x1,y1=y1,z1=h1,x2=x2,y2=y2,z2=h2,distance=distance)
