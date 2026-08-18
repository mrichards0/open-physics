import random
def generate(data):
    a=random.choice([1.2,1.4,1.67,1.8,2.0]); b=random.choice([8.5,9.0,9.11,9.5])
    data["params"].update(a_coeff=a,b_coeff=b); data["correct_answers"]["ratio"]=a/b*1e4
