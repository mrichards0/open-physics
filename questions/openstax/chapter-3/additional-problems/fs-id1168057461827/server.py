import math,random
def generate(data):
 h=random.randint(50,300); g=random.choice([9.8,9.81]); data["params"].update(h=h,g=g); data["correct_answers"]["speed"]=math.sqrt(2*g*h)
