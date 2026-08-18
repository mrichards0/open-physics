import math, random
def generate(data):
    f = random.randrange(20, 151) / 10
    rcm = random.randrange(40, 151) / 10
    omega = 2*math.pi*f
    data["params"].update(rate=f, radius_cm=rcm)
    data["correct_answers"].update(omega=omega, accel=omega*omega*rcm/100)
