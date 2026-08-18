import math,random
def generate(data):
 green=random.randint(50,120); drop=random.randint(5,35); v0=random.randint(15,35); a=random.randint(25,55); g=random.choice([9.8,9.81]); vx=v0*math.cos(math.radians(a)); vy=v0*math.sin(math.radians(a)); t=(vy+math.sqrt(vy*vy+2*g*drop))/g; x=vx*t; miss=x-green
 data["params"].update(green=green,drop=drop,v0=v0,angle=a,g=g); data["correct_answers"].update(time=t,x=x,signed=miss,distance=abs(miss))
