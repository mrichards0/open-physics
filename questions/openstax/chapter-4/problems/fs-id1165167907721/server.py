import math,random
def generate(data):
 x=random.randint(400,1600); drop=random.randint(200,1200); a=random.randint(25,60); g=random.choice([3.7,9.8,9.81]); den=2*math.cos(math.radians(a))**2*(x*math.tan(math.radians(a))+drop); v=math.sqrt(g*x*x/den)
 data["params"].update(x=x,drop=drop,angle=a,g=g); data["correct_answers"].update(speed=v,time=x/(v*math.cos(math.radians(a))))
