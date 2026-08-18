import random
def generate(data):
 v=random.randrange(10,51)*1e6; exponent=random.choice([-3,-4,-5,-6]); factor=random.choice([1,2,4,5]); t=factor*10**exponent; data["params"].update(v=v,t=t); data["correct_answers"]["acceleration"]=v/t
