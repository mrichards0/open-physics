import random
def generate(data):
 km=random.randrange(5,31)/10; L=km*1000; t1=random.randint(30,100); t2=t1+random.randint(10,80); a=2*L*(1/t2-1/t1)/(t1+t2); vi=L/t1-0.5*a*t1; vf=vi+a*(t1+t2)
 data["params"].update(km=km,t1=t1,t2=t2); data["correct_answers"].update(acceleration=a,initial=vi,final=vf)
