import random
def generate(data):
    a=random.choice([1.5,1.8,2.0,2.2,2.5]); b=random.choice([2.0,2.05,2.5,3.0]); c=random.choice([3.0,3.1,3.5,4.0]); da=random.choice([0.01,0.02,0.05,0.1]); db=random.choice([0.01,0.02,0.05]); dc=random.choice([0.02,0.05,0.1]); v=a*b*c
    data["params"].update(a=a,b=b,c=c,da=da,db=db,dc=dc); data["correct_answers"].update(volume=v,uncertainty=v*(da/a+db/b+dc/c))
