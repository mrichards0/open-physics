import random
def generate(data):
 a=random.choice([i for i in range(-6,7) if i]); b=random.choice([i for i in range(-5,6) if i]); y=random.randint(-10,10); t=random.randrange(5,41)/10
 data["params"].update(a=a,b=b,y=y,t=t); data["correct_answers"].update(v0x=0,v0y=0,v0z=0,vtx=2*a*t,vty=0,vtz=3*b*t*t,vax=a*t,vay=0,vaz=b*t*t)
