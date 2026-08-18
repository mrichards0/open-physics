import math,random
def generate(data):
 v0=random.randrange(10,81)/10; release=random.randint(20,120); g=random.choice([9.8,9.81]); h=v0*release; t=(v0+math.sqrt(v0*v0+2*g*h))/g
 data["params"].update(v0=v0,release=release,g=g); data["correct_answers"].update(time=t,velocity=v0-g*t)
