import random
def generate(data):
 x0=random.randint(-20,20); v0=random.randint(-10,10); a=random.choice([i for i in range(-12,13) if i]); t=random.randint(1,10); data["params"].update(x0=x0,v0=v0,a=a,t=t); data["correct_answers"]["position"]=x0+v0*t+0.5*a*t*t
