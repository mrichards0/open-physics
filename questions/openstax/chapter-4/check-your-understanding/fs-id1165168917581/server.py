import math,random
def generate(data):
 r=random.randrange(50,501)/10; ac=random.randrange(100,2001,10); v=math.sqrt(ac*r); data["params"].update(r=r,ac=ac); data["correct_answers"].update(cms=v,ms=v/100)
