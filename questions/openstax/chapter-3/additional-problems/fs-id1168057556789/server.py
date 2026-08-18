import random
def generate(data):
 t=random.randrange(20,101)/100; g=random.choice([9.8,9.81]); denominator=random.choice([5,6,7]); f=1/denominator; data["params"].update(t=t,g=g,fraction=f); data["correct_answers"].update(earth=0.5*g*t*t,moon=0.5*g*f*t*t)
