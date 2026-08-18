import random
def generate(data):
    f=[random.choice([i for i in range(-5,6) if i]) for _ in range(3)]; t=random.randint(2,8)
    r=[random.randint(-20,20) for _ in range(3)]; v=[random.randint(-12,12) for _ in range(3)]; a=[random.randint(-5,5) for _ in range(3)]
    o=[0.5*x*t*t for x in f]; uf=[x*t for x in f]
    data["params"].update(fx=f[0],fy=f[1],fz=f[2],t=t,rx=r[0],ry=r[1],rz=r[2],vx=v[0],vy=v[1],vz=v[2],ax=a[0],ay=a[1],az=a[2])
    data["correct_answers"].update(ox=o[0],oy=o[1],oz=o[2],rx=r[0]+o[0],ry=r[1]+o[1],rz=r[2]+o[2],vx=v[0]+uf[0],vy=v[1]+uf[1],vz=v[2]+uf[2],ax=a[0]+f[0],ay=a[1]+f[1],az=a[2]+f[2])
