import math,random
def generate(data):
 h=random.randint(100,500); v0=random.randint(5,20); g=random.choice([9.8,9.81]); impact=(v0+math.sqrt(v0*v0+2*g*h))/g; te=random.randrange(5,int((impact-0.2)*10))/10
 data["params"].update(h=h,v0=v0,g=g,teval=te); data["correct_answers"].update(maximum=h+v0*v0/(2*g),position=h+v0*te-0.5*g*te*te,velocity=v0-g*te,impact_time=impact)
