import random
def generate(data):
 v=random.randrange(60,181)/10; d=random.randrange(120,501)/100; g=random.choice([9.8,9.81]); data["params"].update(v=v,d=d,g=g); data["correct_answers"]["drop"]=0.5*g*(d/v)**2
