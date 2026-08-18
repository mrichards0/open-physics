import random
def generate(data):
 v=random.randint(25,50); d=random.randrange(120,201)/10; g=random.choice([9.8,9.81]); t=d/v; data["params"].update(v=v,d=d,g=g); data["correct_answers"].update(time=t,drop=0.5*g*t*t)
