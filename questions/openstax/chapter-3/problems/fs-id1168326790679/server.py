import random
def generate(data):
 dt=[random.randint(2,6) for _ in range(3)]; v=[random.choice([i for i in range(-6,7) if i]) for _ in range(3)]; x0=random.randint(-10,10); t1=dt[0]; t2=t1+dt[1]; t3=t2+dt[2]; x1=x0+v[0]*dt[0]; x2=x1+v[1]*dt[1]; x3=x2+v[2]*dt[2]
 data["params"].update(t1=t1,t2=t2,t3=t3,x0=x0,x1=x1,x2=x2,x3=x3); data["correct_answers"].update(v1=v[0],v2=v[1],v3=v[2])
