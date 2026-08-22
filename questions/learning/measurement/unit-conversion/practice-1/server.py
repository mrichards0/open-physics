import random


def generate(data):
    speed = random.choice([36, 45, 54, 63, 72, 81, 90, 99, 108])
    data["params"]["speed"] = speed
    data["correct_answers"].update(meters_per_second=speed / 3.6, seconds_factor=3600, meters_factor=1000)
