import random
from spiritsfire_physics.units import conversion


def generate(data):
    value = random.randint(12, 95) / 10
    case = conversion(value, "km", "m", 1000)
    data["params"].update(value=value)
    data["correct_answers"].update(numerator_number=1000, denominator_number=1, converted=case.result)
