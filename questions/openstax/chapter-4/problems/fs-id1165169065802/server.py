import math, random
def generate(data):
    r_million = random.randrange(500, 2501) / 10
    days = random.randrange(500, 7001) / 10
    r = r_million*1e9
    period = days*86400
    data["params"].update(radius_million=r_million, days=days)
    data["correct_answers"]["accel"] = 4*math.pi**2*r/period**2
