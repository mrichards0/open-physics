import random

CHOICES=[('ks', 3), ('ms', -3), ('us', -6), ('ns', -9), ('Ms', 6)]

def generate(data):
    unit, power = random.choice(CHOICES)
    coefficient = random.choice([1.2, 2.5, 3.75, 4.8, 6.4, 7.25, 9.5])
    scale = random.choice([1, 10, 100])
    value = coefficient * scale
    base_value = value * 10 ** power
    data["params"].update(value=value, base_value=base_value, unit=unit, prefix_power=power)
    data["correct_answers"]["converted_value"] = value
