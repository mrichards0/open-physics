import random
def generate(data):
 v0=random.randrange(5,41)/10; t=random.randrange(10,41)/10; g=random.choice([9.8,9.81]); data["params"].update(v0=v0,t=t,g=g); data["correct_answers"]["height"]=v0*t+0.5*g*t*t
