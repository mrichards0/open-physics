import math,random
def generate(data):
 r=random.randint(7000,60000); T=random.randrange(10,501)/10; R=r*1000; ts=T*3600; v=2*math.pi*R/ts; data["params"].update(radius=r,period=T); data["correct_answers"].update(speed=v,accel=v*v/R)
