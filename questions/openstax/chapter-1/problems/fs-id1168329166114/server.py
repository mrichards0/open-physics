import random
def generate(data):
    life=random.choice([60,66,72,75,78,81,84,90]); elapsed=random.choice([1000,1500,1800,2000,2025,2500,3000])
    data["params"].update(lifetime=life,elapsed_years=elapsed); data["correct_answers"]["generations"]=elapsed/(life/3)
