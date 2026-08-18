import random
def generate(data):
 v=random.choice([i for i in range(-40,41) if i]); t1=random.randint(0,10); t2=t1+random.randint(1,12); data["params"].update(v=v,t1=t1,t2=t2); data["correct_answers"]["displacement"]=v*(t2-t1)
