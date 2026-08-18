import random
def generate(data):
    u=random.choice([0.1,0.2,0.25,0.5,0.75,1.0]); d=random.choice([5,10,15,20,25,30])
    data["params"].update(uncertainty_cm=u,distance_m=d); data["correct_answers"]["percent"]=100*u/(d*100)
