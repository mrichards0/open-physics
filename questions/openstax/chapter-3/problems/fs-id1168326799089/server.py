import random
def generate(data):
 dt=random.randint(2,6); v1=random.randint(5,12); v2=0; v3=-random.randint(2,10); v4=random.randint(1,v1-1); vs=(v1,v2,v3,v4); data["params"].update(dt=dt,**{f"dx{i}":v*dt for i,v in enumerate(vs,1)}); data["correct_answers"].update(**{f"v{i}":v for i,v in enumerate(vs,1)})
