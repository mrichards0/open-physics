import math,random
def generate(data):
 h=random.randrange(100,501)/100; g=random.choice([9.8,9.81]); v=math.sqrt(2*g*h); data["params"].update(h=h,g=g); data["correct_answers"].update(speed=v,time=2*v/g)
