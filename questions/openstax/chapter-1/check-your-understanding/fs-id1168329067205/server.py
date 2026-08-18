import random

def generate(data):
    unit, power = random.choice([("Mg", 3), ("Gg", 6)])
    exponent = power + random.choice([0, 1, 2])
    coefficient = random.choice([1.25, 2.4, 3.75, 4.8, 6.2, 7.5, 9.1])
    data["params"].update(coefficient=coefficient, exponent=exponent, unit=unit, unit_kg_power=power)
    data["correct_answers"]["converted_mass"] = coefficient * 10 ** (exponent - power)
