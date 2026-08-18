import random
def generate(data):
 t1=random.randrange(5,41)/10; t2=t1+random.randrange(5,51)/10; v1=random.randrange(-100,151)/10; v2=random.randrange(-150,101)/10; data["params"].update(v1=v1,v2=v2,t1=t1,t2=t2); data["correct_answers"]["acceleration"]=(v2-v1)/(t2-t1)
