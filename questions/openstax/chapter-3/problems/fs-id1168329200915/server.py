import random
def generate(data):
 v=random.randrange(40,121)/10; d=random.randrange(15,81)/100; data["params"].update(v=v,d=d); data["correct_answers"].update(acceleration=-v*v/(2*d),time=2*d/v)
