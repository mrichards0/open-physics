import math,random
def generate(data):
 v=[random.randint(-300,300) for _ in range(3)]; a=[random.randint(-15,15) for _ in range(3)]; t=random.randint(2,20); f=[v[k]+a[k]*t for k in range(3)]; data["params"].update(vx=v[0],vy=v[1],vz=v[2],ax=a[0],ay=a[1],az=a[2],time=t); data["correct_answers"].update(fx=f[0],fy=f[1],fz=f[2],speed=math.sqrt(sum(x*x for x in f)))
