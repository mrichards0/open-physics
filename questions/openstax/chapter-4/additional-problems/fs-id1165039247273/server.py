import math,random
def generate(data):
 lat=random.randint(0,75); R=random.randint(3000,8000); T=random.randrange(100,401)/10; g=random.randrange(40,151)/10; axis=R*math.cos(math.radians(lat)); omega=2*math.pi/(T*3600); a=omega*omega*axis*1000
 data["params"].update(latitude=lat,radius=R,period=T,g=g); data["correct_answers"].update(axis=axis,accel=a,ratio=a/g)
