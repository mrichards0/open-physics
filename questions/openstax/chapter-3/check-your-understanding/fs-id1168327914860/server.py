import math,random
def generate(data):
 h=random.randrange(100,1001)/10; g=random.choice([9.8,9.81]); data["params"].update(h=h,g=g); data["correct_answers"]["time"]=math.sqrt(2*h/g)
