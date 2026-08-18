import random
def generate(data):
 v0=random.randrange(10,101)/10; a=random.randrange(20,101)/1000; minutes=random.randrange(20,121)/10; b=random.randrange(20,101)/100; t=60*minutes; vf=v0+a*t
 data["params"].update(v0=v0,a=a,minutes=minutes,brake=b); data["correct_answers"].update(vf=vf,tb=vf/b,d1=0.5*(v0+vf)*t,d2=vf*vf/(2*b))
