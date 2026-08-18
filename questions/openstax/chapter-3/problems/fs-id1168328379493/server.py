import random
def generate(data):
 v0=random.randint(8,22); g=random.choice([9.8,9.81]); data["params"].update(v0=v0,g=g); data["correct_answers"].update(height=v0*v0/(2*g),time=2*v0/g)
