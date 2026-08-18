import math,random
def generate(data):
 h=random.randint(50,180); v0=random.randint(20,50); a=random.randint(30,65); g=random.choice([9.8,9.81]); vx=v0*math.cos(math.radians(a)); vy=v0*math.sin(math.radians(a)); impact=(vy+math.sqrt(vy*vy+2*g*h))/g; ts=[impact*f for f in (0.25,0.5,0.75)]; ans=dict(rise=vy*vy/(2*g),xapex=vx*vy/g,time=impact,range=vx*impact)
 p=dict(h=h,v0=v0,angle=a,g=g)
 for i,t in enumerate(ts,1): p[f"t{i}"]=t; ans[f"x{i}"]=vx*t; ans[f"y{i}"]=vy*t-0.5*g*t*t
 data["params"].update(p); data["correct_answers"].update(ans)
