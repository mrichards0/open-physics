import random
def generate(data):
    rho=random.choice([0.8,1.0,1.2,2.7,4.5,7.8,8.9,11.3]); data["params"]["g_cm3"]=rho; data["correct_answers"]["kg_m3"]=rho*1000
