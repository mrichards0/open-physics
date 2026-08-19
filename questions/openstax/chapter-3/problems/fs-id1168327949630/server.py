import random

from spiritsfire_physics.kinematics import acceleration_case


def generate(data):
    case = acceleration_case(random, "independent")
    data["params"].update(case.params(), v=case.final_velocity, t=case.elapsed_time)
    data["correct_answers"]["acceleration"] = case.acceleration
