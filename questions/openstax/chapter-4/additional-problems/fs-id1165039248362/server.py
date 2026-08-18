import random
def generate(data):
 i=[random.randint(-50,50)/10 for _ in range(3)]; d=[random.randint(-50,50)/10 for _ in range(3)]; data["params"].update(ix=i[0],iy=i[1],iz=i[2],dx=d[0],dy=d[1],dz=d[2]); data["correct_answers"].update(x=i[0]+d[0],y=i[1]+d[1],z=i[2]+d[2])
