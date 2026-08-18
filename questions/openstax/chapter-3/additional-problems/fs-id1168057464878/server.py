import math,random
def generate(data):
 v=random.randrange(20,61)/10; gap=random.randint(20,100); a=random.randrange(2,21)/100; t=math.sqrt(2*gap/a); data["params"].update(v=v,gap=gap,a=a); data["correct_answers"].update(time=t,distance=v*t+0.5*a*t*t,speed=v+a*t)
