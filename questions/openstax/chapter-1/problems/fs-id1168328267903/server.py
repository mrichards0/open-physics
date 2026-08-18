import math,random
def generate(data):
    d=random.choice([1.205,1.508,2.104,2.506,3.102,3.504,4.208,5.006]); data["params"]["diameter"]=d; data["correct_answers"]["area"]=math.pi*(d/2)**2
