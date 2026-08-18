import math,random
def generate(data):
 r=random.randrange(40,151)/10; a=random.randint(10,40); g=random.choice([9.8,9.81]); v=math.sqrt(r*g/math.sin(math.radians(2*a))); data["params"].update(range=r,angle=a,g=g); data["correct_answers"].update(speed=v,time=2*v*math.sin(math.radians(a))/g)
