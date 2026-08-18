import math,random
def generate(data):
 v0=random.randint(0,12); a=random.randint(1,10); t=random.randrange(5,51)/10; dx=v0*t+0.5*a*t*t; solved=(-v0+math.sqrt(v0*v0+2*a*dx))/a; data["params"].update(v0=v0,a=a,dx=dx); data["correct_answers"].update(time=solved,velocity=v0+a*solved)
