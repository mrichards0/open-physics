import random
def generate(data):
 x0=random.randint(-10,10); c=random.choice([i for i in range(-8,9) if i]); t1=random.randint(1,5); t2=t1+random.randint(1,5); data["params"].update(x0=x0,c=c,t1=t1,t2=t2); data["correct_answers"].update(v1=2*c*t1,a1=2*c,v2=2*c*t2,a2=2*c)
