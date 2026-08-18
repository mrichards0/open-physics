import random
def generate(data):
 dt=random.randint(2,6); a1=random.randint(5,12); a2=0; a3=-random.randint(2,10); a4=random.randint(1,a1-1); aa=(a1,a2,a3,a4); data["params"].update(dt=dt,**{f"dv{i}":a*dt for i,a in enumerate(aa,1)}); data["correct_answers"].update(**{f"a{i}":a for i,a in enumerate(aa,1)})
