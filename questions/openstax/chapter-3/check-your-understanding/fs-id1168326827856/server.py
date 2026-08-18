import random
def generate(data):
 v=random.randint(4,15); t=random.randrange(10,61,5); data["params"].update(v=v,t=t); data["correct_answers"]["acceleration"]=2*v/t
