import random
def generate(data):
 d=random.randrange(100,501)/10; m=random.randint(4,20); kmh=d/(m/60); data["params"].update(distance=d,minutes=m); data["correct_answers"].update(kmh=kmh,ms=kmh/3.6)
