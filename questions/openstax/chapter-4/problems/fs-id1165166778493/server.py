import math, random
def generate(data):
    v = random.randrange(80, 301) / 10
    angle = random.randint(20, 70)
    factor = random.choice([0.25, 0.5, 1.5, 2, 2.5, 3])
    ratio = math.sqrt(factor)
    data["params"].update(speed=v, angle=angle, factor=factor)
    data["correct_answers"].update(speed2=v*ratio, ratio=ratio)
