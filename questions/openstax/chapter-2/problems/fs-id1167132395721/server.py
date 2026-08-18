import math,random
def generate(data):
 b=random.randrange(50,201,10); a=random.randrange(20,61,5); data["params"].update(baseline=b,angle=a); data["correct_answers"]["width"]=b*math.tan(math.radians(a))
