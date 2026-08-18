import random
def generate(data):
    u=[random.randint(-8,8) for _ in range(3)]; t=random.randint(2,10)
    r=[random.randint(-30,30) for _ in range(3)]; v=[random.randint(-15,15) for _ in range(3)]; a=[random.randint(-6,6) for _ in range(3)]
    o=[x*t for x in u]
    data["params"].update(ux=u[0],uy=u[1],uz=u[2],t=t,rx=r[0],ry=r[1],rz=r[2],vx=v[0],vy=v[1],vz=v[2],ax=a[0],ay=a[1],az=a[2])
    data["correct_answers"].update(ox=o[0],oy=o[1],oz=o[2],rx=r[0]+o[0],ry=r[1]+o[1],rz=r[2]+o[2],vx=v[0]+u[0],vy=v[1]+u[1],vz=v[2]+u[2],ax=a[0],ay=a[1],az=a[2])
