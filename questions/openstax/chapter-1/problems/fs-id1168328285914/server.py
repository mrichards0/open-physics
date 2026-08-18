import random


def generate(data):
    """Generate speeds clearly above or below a realistic posted limit."""
    speed_limit_kph = random.choice([80, 90, 100, 110])
    limit_mps = speed_limit_kph / 3.6
    candidates = [value for value in range(12, 39) if abs(value - limit_mps) >= 1.5]
    speed_mps = random.choice(candidates)
    speed_kph = speed_mps * 3.6
    data["params"]["speed_mps"] = speed_mps
    data["params"]["speed_limit_kph"] = speed_limit_kph
    data["correct_answers"]["speed_kph"] = speed_kph
    data["correct_answers"]["limit_difference"] = speed_kph - speed_limit_kph
