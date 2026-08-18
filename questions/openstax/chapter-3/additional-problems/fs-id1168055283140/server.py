import random
def generate(data):
 v=random.randint(5,12); d=random.randrange(3,11)/10; maximum=v*v/(2*d); finish=random.randint(int(maximum)+5,int(maximum)+80); data["params"].update(v=v,decel=d,finish=finish); data["correct_answers"].update(maximum=maximum,shortfall=finish-maximum)
