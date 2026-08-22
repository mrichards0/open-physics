import random


def generate(data):
    density = random.randint(65, 180) / 100
    data["params"]["density"] = density
    data["correct_answers"]["kilograms_per_cubic_meter"] = density * 1000
