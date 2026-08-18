import random
def generate(data):
    duration=random.choice([0.5,1,1.5,2,2.5,4,5,8,10]); data["params"]["duration_ms"]=duration; data["correct_answers"]["rate"]=1/(duration*1e-3)
