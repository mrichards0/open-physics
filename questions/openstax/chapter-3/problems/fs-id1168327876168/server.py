import math,random
def generate(data):
 h=random.randrange(50,251)/100; g=random.choice([9.8,9.81]); data["params"].update(h=h,g=g); data["correct_answers"]["velocity"]=math.sqrt(2*g*h)
