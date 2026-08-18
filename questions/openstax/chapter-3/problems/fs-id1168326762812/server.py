import random
def generate(data):
 x0=random.randint(-20,20); v=random.choice([i for i in range(-12,13) if i]); data["params"].update(x0=x0,v=v); data["correct_answers"]["velocity"]=v
