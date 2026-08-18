import random
def generate(data):
    m=random.randrange(45,101); rho=random.choice([980,990,1000,1010,1020])
    data["params"].update(mass_kg=m,density=rho); data["correct_answers"]["volume_l"]=m/rho*1000
