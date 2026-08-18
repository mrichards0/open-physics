import random
def generate(data):
    p=[random.randint(-12,12) for _ in range(3)]; ab=[random.randint(-10,10) for _ in range(3)]; bc=[random.randint(-10,10) for _ in range(3)]
    data["params"].update(px=p[0],py=p[1],pz=p[2],abx=ab[0],aby=ab[1],abz=ab[2],bcx=bc[0],bcy=bc[1],bcz=bc[2])
    data["correct_answers"].update(vx=p[0]+ab[0]+bc[0],vy=p[1]+ab[1]+bc[1],vz=p[2]+ab[2]+bc[2])
