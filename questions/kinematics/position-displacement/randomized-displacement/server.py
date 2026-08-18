import random


def generate(data):
    """Generate integer positions with nonzero, signed displacement."""
    x0 = random.randint(-20, 20)
    displacement = random.choice([value for value in range(-20, 21) if value != 0])
    xf = x0 + displacement

    data["params"]["x0"] = x0
    data["params"]["xf"] = xf
    data["correct_answers"]["displacement"] = displacement
