import random


def generate(data):
    side = random.randint(12, 48) / 10
    data["params"]["side"] = side
    data["correct_answers"].update(linear_factor=100, volume_cm3=(side * 100) ** 3)
