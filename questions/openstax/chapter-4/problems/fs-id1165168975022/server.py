import math, random
def generate(data):
    r = random.randrange(30, 151) / 10
    k = random.choice([0.5, 0.75, 1, 1.25, 1.5, 2])
    g = random.choice([9.8, 9.81])
    v = math.sqrt(k*g*r)
    data["params"].update(radius=r, multiple=k, g=g)
    data["correct_answers"].update(speed=v, rpm=60*v/(2*math.pi*r))
