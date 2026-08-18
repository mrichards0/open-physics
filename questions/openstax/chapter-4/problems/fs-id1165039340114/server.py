import math, random
def generate(data):
    boat=random.randrange(50,151)/10; current=random.randrange(10,int(boat*7))/10; along=random.randrange(5,51)/10; width=random.randrange(3,31)/10
    cross=math.sqrt(boat*boat-current*current)
    data["params"].update(boat=boat,current=current,along=along,width=width)
    data["correct_answers"].update(down=along/(boat+current),up=along/(boat-current),angle=math.degrees(math.asin(current/boat)),cross_speed=cross,cross_time=width/cross,aim_time=width/boat,drift=current*width/boat)
