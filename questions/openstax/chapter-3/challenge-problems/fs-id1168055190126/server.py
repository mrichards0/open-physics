import random
def generate(data):
 a=random.randint(2,12); b=random.randrange(5,41)/10; te=random.randrange(2,61)/10; tz=2*a/(3*b); x=lambda t:a*t*t-b*t**3
 data["params"].update(a=a,b=b,te=te); data["correct_answers"].update(c1=2*a,c2=-3*b,d0=2*a,d1=-6*b,velocity=2*a*te-3*b*te*te,acceleration=2*a-6*b*te,tmax=tz,tzero=tz,xmax=x(tz))
