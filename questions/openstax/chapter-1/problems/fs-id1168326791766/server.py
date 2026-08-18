import random
def generate(data):
    rate=random.choice([0.5,1,2,3,4]); years=random.randrange(60,101,5); c=random.choice([1,2,5,8]); e=random.choice([14,15,16,17])
    ops=rate*years*365.25*86400; data["params"].update(human_rate=rate,years=years,super_coeff=c,super_exp=e)
    data["correct_answers"].update(human_ops=ops,computer_seconds=ops/(c*10**e))
