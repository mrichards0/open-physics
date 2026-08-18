import math,random
def generate(data):
 a,b=random.randint(2,20),random.randint(2,20); p=random.randrange(10,171,10); c=math.sqrt(a*a+b*b+2*a*b*math.cos(math.radians(p)))
 data["params"].update(a=a,b=b,phi=p); data["correct_answers"]["c"]=c
