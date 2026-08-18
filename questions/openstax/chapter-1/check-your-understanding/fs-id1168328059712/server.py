import random


def generate(data):
    """Generate a force and convert pound-force to newtons deterministically."""
    force_lbf = random.randint(10, 200)
    data["params"]["force_lbf"] = force_lbf
    data["correct_answers"]["force_newtons"] = force_lbf * 4.45
