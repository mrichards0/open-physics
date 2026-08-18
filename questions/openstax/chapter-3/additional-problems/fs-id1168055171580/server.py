import random
def generate(data):
 v=random.randint(15,45); d=random.randint(500,1800); data["params"].update(v=v,d=d); data["correct_answers"]["acceleration"]=-v*v/d
