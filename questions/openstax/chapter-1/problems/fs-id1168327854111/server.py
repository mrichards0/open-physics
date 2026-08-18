import random
def generate(data):
    kmh=random.randrange(60,131,5); data["params"]["kmh"]=kmh
    data["correct_answers"].update(mps=kmh/3.6,mph=kmh*0.62137119223733)
