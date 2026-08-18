import random
def generate(data):
    years=random.randrange(60,101,5); c=random.choice([1,2,5,8]); e=random.randint(-24,-12)
    data["params"].update(years=years,coefficient=c,exponent=e); data["correct_answers"]["ratio"]=years*365.25*86400/(c*10**e)
