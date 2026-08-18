import math,random
def generate(data):
 h=random.randint(10,100); km=random.randrange(5,301)/10; a=random.randint(10,60); L=km*1000; x=L*math.cos(math.radians(a)); y=h+L*math.sin(math.radians(a)); data["params"].update(h=h,km=km,angle=a); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),direction=math.degrees(math.atan2(y,x)))
