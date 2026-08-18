import random
def generate(data):
 v=random.randint(30,80); d=random.randrange(10,61)/10; data["params"].update(v=v,d=d); data["correct_answers"]["acceleration"]=-v*v/(2*d)
