import random
def generate(data):
    c=random.choice([0.4535,0.4536,0.4539,0.4540]); dc=random.choice([0.00005,0.0001,0.0002]); target=random.choice([0.5,1,2,5])
    data["params"].update(kg_per_lbm=c,conversion_uncertainty=dc,target_kg=target); data["correct_answers"].update(percent=100*dc/c,mass_lbm=target/dc)
