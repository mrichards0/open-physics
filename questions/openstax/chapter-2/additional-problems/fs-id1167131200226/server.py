import math,random
def generate(data):
 r=random.randint(2,20); p=random.choice([a for a in range(10,351,10) if a%90]); t=math.radians(p); x=r*math.cos(t); y=r*math.sin(t)
 polar=lambda x,y:(math.hypot(x,y),math.degrees(math.atan2(y,x))%360)
 ra,aa=polar(-x,y); rb,ab=polar(-2*x,-2*y); rc,ac=polar(3*x,-3*y)
 data["params"].update(r=r,phi=p); data["correct_answers"].update(ra=ra,aa=aa,rb=rb,ab=ab,rc=rc,ac=ac)
