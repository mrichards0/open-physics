import random
def generate(data):
 v=random.randint(20,50); a=random.randrange(20,81)/10; data["params"].update(v=v,a=a); data["correct_answers"]["time"]=2*v/a
