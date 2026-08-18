import math,random
def generate(data):
 v0=random.randrange(20,81)/10; h=random.randrange(100,501)/100; g=random.choice([9.8,9.81]); t=(v0+math.sqrt(v0*v0+2*g*h))/g
 data["params"].update(v0=v0,h=h,g=g); data["correct_answers"].update(rise=v0*v0/(2*g),time=t,velocity=v0-g*t)
