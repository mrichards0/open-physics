import random
def generate(data):
    k=random.choice([1.0,1.01,1.03,1.05]); r=random.choice([80,100,120,130,150,180]); t=random.choice([15,20,25,30,40,50]); rho=random.choice([1.15,1.2,1.25,1.3]); ts=t/1000; energy=rho*r**5/(k**5*ts**2)
    data["params"].update(k=k,radius=r,time_ms=t,density=rho); data["correct_answers"].update(a=0.2,b=-0.2,c=0.4,energy=energy,kilotons=energy/4.2e12)
