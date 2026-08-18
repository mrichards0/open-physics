import math,random
def generate(data):
 d=random.choice([3,4,5,6,7.5,8,10]); a=random.randrange(10,81,5); e=d*math.cos(math.radians(a)); n=d*math.sin(math.radians(a)); data["params"].update(distance=d,angle=a); data["correct_answers"].update(east=e,north=n,extra=e+n-d)
