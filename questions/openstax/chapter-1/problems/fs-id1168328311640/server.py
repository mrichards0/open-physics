import random
def generate(data):
    c=random.choice([1,2.5,4,6,8]); e=random.randint(14,19); rho=c*10**e
    data["params"].update(coefficient=c,exponent=e); data["correct_answers"]["density"]=rho*1e-12
