import random
def generate(data):
    distance = random.choice([100, 200, 300, 400])
    time = random.randrange(int(distance/12*10), int(distance/5*10)) / 10
    radius = random.randrange(150, 501) / 10
    v = distance/time
    data["params"].update(distance=distance, time=time, radius=radius)
    data["correct_answers"].update(speed=v, accel=v*v/radius)
