import random


def generate(data):
    vi = random.randint(8, 26)
    delta_v = random.choice([value for value in range(-16, 17) if abs(value) >= 5])
    vf = vi + delta_v
    if vf < 1:
        vf = 1
        delta_v = vf - vi
    dt = random.randint(2, 9)
    acceleration = delta_v / dt
    data["params"].update(
        vi=vi,
        vf=vf,
        dt=dt,
        delta_v=delta_v,
        acceleration=round(acceleration, 4),
    )
    data["correct_answers"].update(delta_v=delta_v, acceleration=acceleration)
