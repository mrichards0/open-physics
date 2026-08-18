import math,random
def generate(data):
    diameter=random.choice([20,40,60,80,100,120,150,200,250,300]); rho=random.choice([900,1000,1100,1200,1300])
    r=diameter*1e-9/2; data["params"].update(diameter_nm=diameter,density=rho); data["correct_answers"]["mass"]=rho*4*math.pi*r**3/3
