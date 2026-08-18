import random
def generate(data):
 dt=[random.randint(2,7) for _ in range(3)]; a=[random.choice([i for i in range(-6,7) if i]) for _ in range(3)]; v0=random.randint(-15,15); t1=dt[0]; t2=t1+dt[1]; t3=t2+dt[2]; v1=v0+a[0]*dt[0]; v2=v1+a[1]*dt[1]; v3=v2+a[2]*dt[2]
 data["params"].update(v0=v0,v1=v1,v2=v2,v3=v3,t1=t1,t2=t2,t3=t3); data["correct_answers"].update(a1=a[0],a2=a[1],a3=a[2])
