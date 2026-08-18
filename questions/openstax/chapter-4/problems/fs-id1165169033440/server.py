import math, random
def generate(data):
    a = random.randrange(10, 501) / 100
    period = random.choice([10, 15, 20, 30, 45, 60])
    omega = 2*math.pi/period
    rcm = a/(omega*omega)
    data["params"].update(accel=a, period=period)
    data["correct_answers"].update(radius_cm=rcm, radius_m=rcm/100)
