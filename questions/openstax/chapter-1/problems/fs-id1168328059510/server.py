import random
def generate(data):
    mps=random.choice([0.5,1,1.5,2,2.5,5,10,15,20,25]); data["params"]["mps"]=mps
    data["correct_answers"].update(kmh=mps*3.6,mph=mps*2.2369362920544)
