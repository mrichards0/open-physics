import math,random
def generate(data):
 a=random.randint(20,70); x=random.randint(20,100); drop=random.randint(5,50); g=random.choice([9.8,9.81]); den=2*math.cos(math.radians(a))**2*(x*math.tan(math.radians(a))+drop); v=math.sqrt(g*x*x/den); data["params"].update(angle=a,distance=x,drop=drop,g=g); data["correct_answers"].update(speed=v,time=x/(v*math.cos(math.radians(a))))
