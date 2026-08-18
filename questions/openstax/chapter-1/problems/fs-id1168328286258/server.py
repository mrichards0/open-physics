import random
def generate(data):
    mass=random.randrange(45,101); percent=random.choice([1,2,2.5,3,4,5])
    data["params"].update(mass=mass,percent=percent); data["correct_answers"]["uncertainty"]=mass*percent/100
