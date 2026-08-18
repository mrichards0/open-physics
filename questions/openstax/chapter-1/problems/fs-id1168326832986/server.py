import random
def generate(data):
    c=random.choice([1,2,5,8]); e=random.randint(12,18); data["params"].update(coefficient=c,exponent=e); data["correct_answers"]["operations"]=c*10**e*365.25*86400
