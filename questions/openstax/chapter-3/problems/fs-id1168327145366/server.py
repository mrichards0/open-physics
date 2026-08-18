import random
def generate(data):
 a=random.randrange(100,501)/100; t=random.randrange(50,201)/10; data["params"].update(a=a,t=t); data["correct_answers"].update(distance=0.5*a*t*t,velocity=a*t)
