import random
def generate(data):
 v=random.randint(40,100); t=random.randint(10,35); data["params"].update(v=v,t=t); data["correct_answers"]["acceleration"]=v/t
