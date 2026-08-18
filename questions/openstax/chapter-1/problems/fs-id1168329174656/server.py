import random
def generate(data):
    l=random.choice([7,8,9,10,11,12]); w=random.choice([5,6,7,8]); h=random.choice([2.5,2.8,3.0,3.2,3.5]); rho=random.choice([1.15,1.2,1.225,1.25])
    data["params"].update(length=l,width=w,height=h,density=rho); data["correct_answers"]["mass"]=rho*l*w*h
