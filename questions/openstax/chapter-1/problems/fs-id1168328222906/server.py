import random
def generate(data):
    mps=random.randint(330,350); data["params"]["mps"]=mps; data["correct_answers"]["kmh"]=mps*3.6
