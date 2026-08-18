import math,random
def generate(data):
 a=random.randint(20,65); x=random.randint(150,500); drop=random.randint(50,500); g=random.choice([9.8,9.81]); v=math.sqrt(g*x*x/(2*math.cos(math.radians(a))**2*(x*math.tan(math.radians(a))+drop))); data["params"].update(angle=a,distance=x,drop=drop,g=g); data["correct_answers"].update(speed=v,time=x/(v*math.cos(math.radians(a))))
