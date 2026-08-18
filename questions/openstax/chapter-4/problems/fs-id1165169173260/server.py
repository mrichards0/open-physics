import math, random
def generate(data):
    rate = random.randrange(20, 601) / 10
    time = random.randrange(50, 601) / 10
    revs = rate*time
    data["params"].update(rate=rate, time=time)
    data["correct_answers"].update(revs=revs, angle=2*math.pi*revs)
