import random


def generate(data):
    """Generate exact petameter/time pairs with realistic signal speeds."""
    time_million_s = random.choice([20, 25, 30, 35, 40])
    speed_hundred_million = random.choice([2.0, 2.4, 2.5, 2.8, 3.0])
    speed = speed_hundred_million * 1e8
    distance_pm = speed * time_million_s * 1e6 / 1e15
    data["params"]["distance_pm"] = round(distance_pm, 2)
    data["params"]["time_million_s"] = time_million_s
    data["correct_answers"]["speed"] = speed
