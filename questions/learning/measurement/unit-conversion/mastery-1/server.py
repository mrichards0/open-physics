import random


def generate(data):
    speed = random.randint(18, 42)
    data["params"]["speed"] = speed
    data["correct_answers"]["kilometers_per_hour"] = speed * 3.6
