import random
def generate(data):
 v=random.randrange(150,401)/10; t=random.randrange(20,81)/10; data["params"].update(v=v,t=t); data["correct_answers"].update(acceleration=v/t,distance=0.5*v*t)
