import math,random
def generate(data):
 e,n=random.randint(2,20),random.randint(2,20); data["params"].update(east=e,north=n); data["correct_answers"].update(magnitude=math.hypot(e,n),angle=math.degrees(math.atan2(n,e)))
