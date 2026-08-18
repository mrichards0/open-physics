import random
def generate(data):
    d=random.choice([0.8,1.0,1.2,1.5,1.8,2.0]); c=random.choice([2.9,3.0,3.1])
    data["params"].update(distance_1e11=d,c_1e8=c); data["correct_answers"]["light_minutes"]=d*1e11/(c*1e8)/60
