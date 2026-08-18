import math,random
def generate(data):
 d=random.randint(10,80); vt=random.randint(40,110); vc=random.randint(30,100); t=d*vt/(vt*vt+vc*vc); sep=math.hypot(-d+vt*t,vc*t); data["params"].update(distance=d,truck=vt,car=vc); data["correct_answers"].update(time_h=t,time_min=60*t,separation=sep)
