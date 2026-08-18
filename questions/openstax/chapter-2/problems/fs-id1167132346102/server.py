import random
def generate(data):
 c=[random.randrange(-15,16,5) for _ in range(2)]; d=[random.randrange(-15,16,5) for _ in range(2)]; f=[random.randrange(-15,16,5) for _ in range(2)]
 data["params"].update(cx=c[0],cy=c[1],dx=d[0],dy=d[1],fx=f[0],fy=f[1]); data["correct_answers"].update(r1x=f[0]-d[0],r1y=f[1]-d[1],r2x=(3*f[0]-c[0]+2*d[0])/5,r2y=(3*f[1]-c[1]+2*d[1])/5)
