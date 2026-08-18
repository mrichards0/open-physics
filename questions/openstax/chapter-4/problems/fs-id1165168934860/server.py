import math, random
def generate(data):
    rpm = random.randrange(600, 6001) / 10
    rcm = random.randrange(30, 301) / 10
    omega = 2*math.pi*rpm/60
    r = rcm/100
    data["params"].update(rpm=rpm, radius_cm=rcm)
    data["correct_answers"].update(omega=omega, speed=omega*r, accel=omega*omega*r)
