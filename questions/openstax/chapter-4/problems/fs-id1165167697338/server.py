import math,random
def generate(data):
 v=random.randrange(20,101)/10; a=random.randint(10,40); g=random.randrange(10,41)/10; T=2*v*math.sin(math.radians(a))/g; data["params"].update(v=v,angle=a,g=g); data["correct_answers"].update(time=T,range=v*math.cos(math.radians(a))*T,height=(v*math.sin(math.radians(a)))**2/(2*g))
