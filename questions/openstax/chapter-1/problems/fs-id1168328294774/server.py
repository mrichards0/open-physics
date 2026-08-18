import math, random
def generate(data):
    r=random.choice([0.6,0.8,1.0,1.2,1.5,1.8,2.0]); days=random.choice([180,240,300,365,450,550,700])
    v=2*math.pi*r*1e11/(days*86400)
    data["params"].update(radius_1e11=r,period_days=days); data["correct_answers"].update(mps=v,mph=v*2.2369362920544)
