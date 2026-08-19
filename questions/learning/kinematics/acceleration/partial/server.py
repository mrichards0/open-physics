import random

from spiritsfire_physics.kinematics import acceleration_case


def generate(data):
    case = acceleration_case(random, "partial")
    data["params"].update(case.params())
    data["correct_answers"].update(case.answers())
