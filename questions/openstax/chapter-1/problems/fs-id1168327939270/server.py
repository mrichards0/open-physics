import random
def generate(data):
    c=random.choice([1.2,2.5,4.0,6.4,8.0]); e=random.randint(15,23); v=c*10**e
    data["params"].update(coefficient=c,exponent=e)
    data["correct_answers"].update(km3=v/1e9,mi3=v/1609.344**3,cm3=v*1e6)
