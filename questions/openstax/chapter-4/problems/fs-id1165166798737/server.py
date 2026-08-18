import math,random
def generate(data):
 v=random.randint(15,35); a=random.randint(5,40); g=random.choice([9.8,9.81]); data["params"].update(v=v,angle=a,g=g); data["correct_answers"].update(range=v*v*math.sin(math.radians(2*a))/g,time=2*v*math.sin(math.radians(a))/g)
