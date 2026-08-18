import random
def generate(data):
    c=random.choice([1,2,5,8]); e=random.randint(12,18); years=random.randrange(60,101,5)
    data["params"].update(coefficient=c,exponent=e,years=years); data["correct_answers"]["operations"]=c*10**e*years*365.25*86400
