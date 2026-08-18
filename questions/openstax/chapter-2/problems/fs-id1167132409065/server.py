import math,random
def generate(data):
 n1,n2,w,ne=[random.randrange(10,71,5) for _ in range(4)]; x=-w+ne/math.sqrt(2); y=n1+n2+ne/math.sqrt(2); rx,ry=-x,-y
 data["params"].update(n1=n1,n2=n2,w=w,ne=ne); data["correct_answers"].update(x=x,y=y,magnitude=math.hypot(x,y),return_x=rx,return_y=ry,return_angle=math.degrees(math.atan2(ry,rx))%360)
