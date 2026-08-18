import math, random
def generate(data):
    plane=random.randint(120,350); wind=random.randint(20,int(plane*0.6)); distance=random.randint(100,800)
    ground=math.sqrt(plane*plane-wind*wind)
    data["params"].update(plane=plane,wind=wind,distance=distance)
    data["correct_answers"].update(angle=math.degrees(math.asin(wind/plane)),ground=ground,time=distance/ground)
