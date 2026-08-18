import random

CHOICES=[('mg', -6), ('g', -3), ('kg', 0), ('Mg', 3), ('Tg', 9), ('ng', -12)]

def generate(data):
    unit, power = random.choice(CHOICES)
    coefficient = random.choice([1.2, 2.5, 3.75, 4.8, 6.4, 7.25, 9.5])
    scale = random.choice([1, 10, 100])
    value = coefficient * scale
    base_value = value * 10 ** power
    data["params"].update(value=value, base_value=base_value, unit=unit, prefix_power=power)
    data["correct_answers"]["base_value"] = base_value
