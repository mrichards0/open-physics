import math,random
def generate(data):
 v=random.randint(80,300); h=random.randrange(80,251)/100; g=random.choice([9.8,9.81]); t=math.sqrt(2*h/g); data["params"].update(v0=v,h=h,g=g); data["correct_answers"].update(time=t,range=v*t)
