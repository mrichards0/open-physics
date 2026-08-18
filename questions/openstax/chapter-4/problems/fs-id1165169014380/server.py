import random
def generate(data):
    r = random.randrange(20, 301) / 10
    v = random.randrange(30, 401) / 10
    data["params"].update(speed=v, radius=r)
    data["correct_answers"]["accel"] = v*v/r
