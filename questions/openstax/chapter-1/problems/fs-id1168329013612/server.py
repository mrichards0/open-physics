import math,random
def generate(data):
    h=random.choice([1.5,1.6,1.7,1.8,1.9,2.0]); r=random.choice([0.12,0.14,0.16,0.18,0.20])
    data["params"].update(height=h,radius=r); data["correct_answers"]["area"]=2*math.pi*r*h+2*math.pi*r*r
