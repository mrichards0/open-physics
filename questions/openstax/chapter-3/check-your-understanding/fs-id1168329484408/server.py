import random
def generate(data):
 a=random.randrange(5,51,5); t=random.randint(5,30); v=a*t; data["params"].update(a=a,v=v); data["correct_answers"]["time"]=t
