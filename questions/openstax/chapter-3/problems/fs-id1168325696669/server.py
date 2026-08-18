import random
def generate(data):
 v=random.randrange(30,101)/10; t=random.randrange(30,121,5); g=random.choice([9.8,9.81]); a=v*1000/t; data["params"].update(v=v,t=t,g=g); data["correct_answers"].update(acceleration=a,multiple=a/g)
