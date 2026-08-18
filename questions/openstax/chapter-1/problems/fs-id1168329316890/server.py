import random
def generate(data):
    g=random.choice([80000,90000,100000,110000,120000]); s=random.choice([1.0,1.5,2.0,2.5,3.0])
    data["params"].update(galaxy_ly=g,system_ly=s); data["correct_answers"]["count"]=(g/s)**2
