import math, random
def generate(data):
    radius = random.randint(2000, 8000)
    g = random.randrange(20, 151) / 10
    v = math.sqrt(g*radius*1000)
    data["params"].update(radius=radius, g=g)
    data["correct_answers"].update(speed=v, kmps=v/1000)
