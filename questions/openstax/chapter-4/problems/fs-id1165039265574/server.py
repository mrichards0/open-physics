import random
def generate(data):
    while True:
        air=random.randrange(60,151)/10; distance=random.randrange(20,121)/10; minutes=random.randrange(100,601)/10
        ground=distance*1000/(minutes*60)
        if 0.2*air < ground < 0.9*air: break
    wind=air-ground; ret=distance*1000/(air+wind)/60
    data["params"].update(air=air,distance=distance,minutes=minutes)
    data["correct_answers"].update({"ground": ground, "wind": wind, "return": ret})
