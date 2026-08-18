import math, random
def generate(data):
    while True:
        v = random.randrange(250, 501) / 10
        g = random.choice([9.8, 9.81])
        rmax = v * v / g
        r = random.randrange(int(0.45 * rmax * 10), int(0.9 * rmax * 10)) / 10
        if 0 < g * r / (v * v) < 1:
            break
    low = math.degrees(math.asin(g * r / (v * v))) / 2
    data["params"].update(speed=v, range=r, g=g)
    data["correct_answers"].update(low=low, high=90-low)
