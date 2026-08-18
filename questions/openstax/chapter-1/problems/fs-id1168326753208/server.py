import random
def generate(data):
    a=random.randint(-25,30); b=random.randint(-30,25)
    while a==b: b=random.randint(-30,25)
    data["params"].update(a_exp=a,b_exp=b,unit=random.choice(["kg","m","s"])); data["correct_answers"]["ratio_exponent"]=a-b
