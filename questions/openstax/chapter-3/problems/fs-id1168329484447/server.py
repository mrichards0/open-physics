import random
def generate(data):
 v0=random.randint(5,15); d=random.randrange(10,41)/10; stop=v0/d; t=random.randrange(int(stop*10)+5,int(stop*10)+31)/10; a=-d
 data["params"].update(v0=v0,decel=d,t=t); data["correct_answers"].update(displacement=v0*t+0.5*a*t*t,velocity=v0+a*t)
