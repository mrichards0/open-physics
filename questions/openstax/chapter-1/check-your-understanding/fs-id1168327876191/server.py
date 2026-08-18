import random

def generate(data):
    diameter_exp = random.randint(3, 8)
    area_exp = 2 * diameter_exp - 6
    data["params"].update(diameter_exp=diameter_exp, area_exp=area_exp)
    data["correct_answers"]["area"] = 10 ** area_exp
