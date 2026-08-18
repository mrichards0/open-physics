import math,random
def generate(data):
 a=random.randint(20,70); T=random.randrange(40,201)/10; g=random.choice([9.8,9.81]); vy=g*T/2; v0=vy/math.sin(math.radians(a)); vx=v0*math.cos(math.radians(a)); te=random.randrange(10,int(T*10))/10; x=vx*te; y=vy*te-0.5*g*te*te
 data["params"].update(angle=a,T=T,g=g,te=te); data["correct_answers"].update(v0=v0,height=vy*vy/(2*g),range=vx*T,x=x,y=y,magnitude=math.hypot(x,y))
