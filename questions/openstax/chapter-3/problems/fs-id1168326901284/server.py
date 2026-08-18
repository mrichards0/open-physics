import random
def generate(data):
 v0=random.randint(-15,30); a=random.choice([i for i in range(-10,11) if i]); t=random.randint(1,10); data["params"].update(v0=v0,a=a,t=t); data["correct_answers"].update(displacement=v0*t+0.5*a*t*t,velocity=v0+a*t)
