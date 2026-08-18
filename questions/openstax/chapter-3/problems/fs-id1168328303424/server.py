import random
def generate(data):
 v=random.randint(15,45); t=random.randrange(30,121)/10; data["params"].update(v=v,t=t); data["correct_answers"]["acceleration"]=v/t
