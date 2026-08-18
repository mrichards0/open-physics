import random
def generate(data):
    rho=random.randrange(800,1301,25); data["params"]["kg_m3"]=rho; data["correct_answers"]["lbm_ft3"]=(rho/0.454)/35.3147
