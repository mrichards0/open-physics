import random
def generate(data):
 p=random.choice([i for i in range(-8,9) if i]); q=random.choice([i for i in range(-10,11) if i]); y=random.randint(-10,10); data["params"].update(p=p,q=q,y=y); data["correct_answers"].update(cx=2*p,cy=0,cz=q,ax=2*p,ay=0,az=0,v0x=0,v0y=0,v0z=q)
