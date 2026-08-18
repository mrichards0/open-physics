import random
def generate(data):
 k=random.randint(1,9); t=random.randrange(5,41)/10; c=-2*k; v=c*t; data["params"].update(k=k,t=t); data["correct_answers"].update(coefficient=c,velocity=v,speed=abs(v))
