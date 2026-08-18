import math,random
def generate(data):
 x=random.randint(1,12); a=random.choice([15,20,25,30,35,40,45,50,55,60,65,70]); t=math.radians(a)
 data["params"].update(x=x,angle=a); data["correct_answers"].update(y=x*math.tan(t),r=x/math.cos(t))
