import random
def generate(data):
 v0=random.randint(2,15); vf=v0+random.randint(15,45); t=random.randrange(100,601)/10000; data["params"].update(v0=v0,vf=vf,t=t); data["correct_answers"]["distance"]=0.5*(v0+vf)*t
