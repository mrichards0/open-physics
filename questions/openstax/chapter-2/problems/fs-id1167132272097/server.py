import math,random
def generate(data):
 a=[random.randint(-10,10) for _ in range(3)]; b=[random.randint(-10,10) for _ in range(3)]; c=[a[i]+b[i] for i in range(3)]; d=[2*a[i]-b[i] for i in range(3)]
 data["params"].update(ax=a[0],ay=a[1],az=a[2],bx=b[0],by=b[1],bz=b[2]); data["correct_answers"].update(cx=c[0],cy=c[1],cz=c[2],cmag=math.sqrt(sum(v*v for v in c)),dx=d[0],dy=d[1],dz=d[2],dmag=math.sqrt(sum(v*v for v in d)))
