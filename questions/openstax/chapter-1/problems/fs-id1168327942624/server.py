import random
def generate(data):
    first=random.choice([100,110,120,130,140]); u=random.choice([1,2,3,4]); second=random.choice([70,80,90,100])
    frac=u/first; data["params"].update(first=first,first_uncertainty=u,second=second)
    data["correct_answers"].update(percent=100*frac,second_uncertainty=second*frac)
