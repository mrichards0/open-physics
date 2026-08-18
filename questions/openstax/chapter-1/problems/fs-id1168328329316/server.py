import random
def generate(data):
    rate=random.randrange(60,161,5); u=random.choice([1,2,3,4,5,6])
    data["params"].update(rate=rate,uncertainty=u); data["correct_answers"]["percent"]=100*u/rate
