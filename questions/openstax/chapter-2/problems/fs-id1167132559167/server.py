import math,random
def generate(data):
 w,n=random.randint(5,40),random.randint(5,40); data["params"].update(west=w,north=n); data["correct_answers"].update(magnitude=math.hypot(w,n),angle=math.degrees(math.atan2(n,w)))
