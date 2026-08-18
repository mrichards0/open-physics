import math,random
def generate(data):
 vi=random.randrange(500,1001)/10; vf=random.randrange(200,int(vi*10))/10; t=random.randrange(10,61)/10; r=random.randint(100,500); at=(vf-vi)/t
 data["params"].update(initial=vi,final=vf,time=t,radius=r); data["correct_answers"].update(tangent=at,start=math.hypot(vi*vi/r,at),end=math.hypot(vf*vf/r,at))
