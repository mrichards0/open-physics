import random
def generate(data):
 x0=random.randint(-10,10); v0=random.randint(-8,8); a=random.choice([i for i in range(-6,7) if i]); t1=random.randint(1,5); t2=t1+random.randint(1,5); data["params"].update(x0=x0,v0=v0,a=a,t1=t1,t2=t2); data["correct_answers"].update(v0=v0,v1=v0+a*t1,v2=v0+a*t2)
