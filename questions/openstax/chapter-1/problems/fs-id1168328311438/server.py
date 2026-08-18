import random
def generate(data):
    first=random.choice([60,70,80,90,100,110,120]); u=random.choice([1,2,3,4]); second=random.choice([40,50,60,70,80,90])
    frac=u/first; data["params"].update(uncertainty=u,first_speed=first,second_speed=second)
    data["correct_answers"].update(percent=100*frac,minimum=second*(1-frac),maximum=second*(1+frac))
