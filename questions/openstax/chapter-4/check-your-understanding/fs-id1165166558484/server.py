import math,random
def generate(data):
 v=random.randint(20,70); a1=random.randint(32,44); a2=random.randint(5,25); g=random.choice([9.8,9.81]); data["params"].update(v=v,a1=a1,a2=a2,g=g); data["correct_answers"].update(r1=v*v*math.sin(math.radians(2*a1))/g,r2=v*v*math.sin(math.radians(2*a2))/g)
