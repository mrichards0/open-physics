import random
def generate(data):
 t=random.randrange(20,101)/10; d=random.randrange(50,601)/10; data["params"].update(t=t,behind=d); data["correct_answers"]["acceleration"]=-2*d/(t*t)
