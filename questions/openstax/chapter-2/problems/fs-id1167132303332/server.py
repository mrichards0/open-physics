import math,random
def generate(data):
 r1,r2=random.choice([2,2.5,3,3.5,4,5]),random.choice([3,3.8,4,4.5,5,6]); a1,a2=random.sample(range(0,360,15),2); x1,y1=r1*math.cos(math.radians(a1)),r1*math.sin(math.radians(a1)); x2,y2=r2*math.cos(math.radians(a2)),r2*math.sin(math.radians(a2))
 data["params"].update(r1=r1,r2=r2,a1=a1,a2=a2); data["correct_answers"].update(x1=x1,y1=y1,x2=x2,y2=y2,distance=math.hypot(x2-x1,y2-y1))
