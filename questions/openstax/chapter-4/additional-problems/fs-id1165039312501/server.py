import random
def generate(data):
 v=random.randrange(50,251)/10; g=random.randrange(10,151)/10; r=v*v/g; data["params"].update(speed=v,range=r); data["correct_answers"].update(gravity=g,angle=45)
